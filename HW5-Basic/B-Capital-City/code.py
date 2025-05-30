"""
Understanding the Problem:

We are given a directed graph of cities, where each node represents a city
and each edge is a one-way road. The goal is to determine which cities 
can be chosen as the capital. For security reasons, the capital must be 
reachable from every other city.

This is equivalent to finding all nodes in a strongly connected component (SCC)
that is a sink in the condensation graph. In a condensed DAG of SCCs, 
a sink SCC has no outgoing edges. If such a sink SCC exists and is unique, 
and every node can reach it (which is implied by it being the only sink), 
then any node in that SCC can be a capital.

In this case, all nodes form one SCC, and all nodes can reach each other,
so any node is a valid capital.

Plan of Attack:

1. Build the Graph and its Reverse:
   - Maintain both the original adjacency list (g)
        and the reversed graph (rg) to prepare for Kosaraju's algorithm.

2. Kosaraju's Algorithm for SCC Detection:
   - First Pass: Run DFS on the original graph to get the finishing order
        of nodes (reverse post-order).
   - Second Pass: Traverse nodes in reverse finishing order
        on the reversed graph to assign component IDs.

3. Build the Condensation DAG:
   - Each SCC becomes a super-node.
   - We build a DAG between SCCs based on connections 
        between them in the original graph.
   - Track the *out-degree* of each SCC.

4. Identify Sink SCC:
   - Collect all SCCs with zero out-degree.
   - If there's exactly one such SCC, its nodes are valid capitals.
   - If there's more than one or none, then no node qualifies.

Output:
- If there's exactly one sink SCC, output the count of nodes in it
  and their 1-based indices in sorted order.
- Else, output 0.

Time Complexity:
- Kosaraju's algorithm runs in O(n + m)
- Condensation DAG construction and 
    sink detection also run in O(n + m)
- Thus, the solution is efficient even 
    for large graphs (n ≤ 10^5, m ≤ 2x10^5)

Edge Cases Handled:
- Disconnected graphs
- All cities in one SCC
- Multiple sink SCCs
- Multiple nodes but no edges

This approach ensures correctness and linear time complexity for large inputs.

References:
1. https://cp-algorithms.com/graph/strongly-connected-components.html
2. https://www.geeksforgeeks.org/strongly-connected-components/
3. Kosaraju's algorithm - Prof Yan Gu Notes Slide: 19-Graph
"""



n, m = map(int, input().split())
g  = [[] for _ in range(n)]
rg = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1; v -= 1
    g[u].append(v)
    rg[v].append(u)

# first pass: iterative DFS for finish order
vis, order = [0]*n, []
for i in range(n):
    if not vis[i]:
        stack = [(i, 0)]
        
        while stack:
            u, phase = stack.pop()
            if phase:
                order.append(u)
        
            else:
                if vis[u]:
                    continue
                vis[u] = 1
                stack.append((u, 1))
        
        
        
                for w in g[u]:
                    if not vis[w]:
                        stack.append((w, 0))

# 2) Second pass: label components
comp = [-1] * n
cid = 0

for u in reversed(order):
    if comp[u] < 0:
        stack = [u]

        while stack:
            x = stack.pop()

            if comp[x] != -1:
                continue
            comp[x] = cid


            for w in rg[x]:
                if comp[w] < 0:
                    stack.append(w)

        cid += 1



# 3) Build out-degree of each component in the condensation DAG
outdeg = [0]*cid
for u in range(n):
    cu = comp[u]
   
    for v in g[u]:
        cv = comp[v]
   
        if cu != cv:
            outdeg[cu] += 1

# 4) Find sinks (zero out-degree)
sinks = [i for i, d in enumerate(outdeg) if d == 0]


if len(sinks) != 1:
    print(0)
    print()

else:
    sc = sinks[0]
    res = [str(i+1) for i, c in enumerate(comp) if c == sc]
    
    
    print(len(res))
    print(" ".join(res))
