"""
Understanding the Problem:

We are given a map of a city as an undirected graph where intersections are nodes 
and roads are edges, each with a cost equal to the number of police vehicles 
required to block that road. The goal is to determine the minimum number of 
vehicles needed to completely block all paths between two specific locations: 
Place A and Place B.

This is equivalent to computing the minimum cut between nodes A and B 
in an undirected weighted graph.

Theoretical Insight:
According to the Max-Flow Min-Cut Theorem, the value of the maximum flow 
from source A to sink B in a flow network is equal to the minimum capacity 
of a set of edges whose removal disconnects A from B.

Hence, we convert the problem to a flow network and solve using Dinic's Algorithm.

Why Dinic's Algorithm:
- Dinic's algorithm is a powerful improvement over Edmonds-Karp.
- It avoids repeatedly traversing saturated paths using a layered BFS + DFS strategy.
- Achieves a time complexity of O(E * sqrt(V)) in general and even better on specific graphs.
- Suitable for large graphs: n ≤ 10^4 nodes, m ≤ 10^5 roads.

Graph Representation Plan:
- Every undirected road (u, v, c) is transformed into two directed edges:
    - u -> v with capacity c
    - v -> u with capacity c
  Each directed edge has a corresponding reverse edge with capacity 0 to support 
  flow reversal in residual graphs. This gives us 4 directed edges per road.

Memory Optimization:
- To handle 4 * 10^5 edges efficiently within 256MB memory:
  - We use array('i') for integers (4 bytes): to[], nxt[], head[].
  - We use array('Q') (8-byte unsigned long long) for capacities: cap[].
  - This compact storage keeps RAM usage well under the 256MB cap.

Key Data Structures:
- head[u]: Index of the first outgoing edge from node u.
- to[e]: Endpoint of edge e.
- cap[e]: Remaining capacity of edge e.
- nxt[e]: Next edge index in the adjacency list of u.
- level[]: Level graph used by BFS to build blocking layers.
- it[]: Pointer to the current edge in DFS to avoid re-scanning dead ends.

Algorithm Plan:
1. Build the directed flow graph using add_edge() for each undirected road.
2. Repeatedly:
   a. Run BFS to build level graph from source A.
   b. Run DFS to send blocking flows from A to B within level graph.
   c. Accumulate the flow.
3. When no more augmenting paths are found, total flow equals the min cut.

Edge Reversal Logic:
- Every edge e has a reverse edge at index e ^ 1.
- When pushing flow through edge e, we decrease cap[e] and increase cap[e^1].

Time and Space Complexity:
- Time: O(E * sqrt(V)) in practice (Dinic's performance).
- Space: O(E) due to compact array-based edge list 

This approach ensures high performance and memory safety for dense, large input graphs.

References:
1. https://cp-algorithms.com/graph/dinic.html
2. https://cp-algorithms.com/graph/edmonds_karp.html
"""


from collections import deque
from array import array

INF = (1 << 63) - 1  


n, m, A, B = map(int, input().split())



head = array('i', [-1]) * (n + 1)
to   = array('i')
cap  = array('Q')
nxt  = array('i')

def add_edge(u: int, v: int, c: int) -> None:
    """
    Adds a directed edge u -> v with capacity c,
    and also adds the reverse edge v -> u with capacity 0.
    """
    # forward edge: index = len(to)
    to.append(v)
    cap.append(c)
    nxt.append(head[u])
    head[u] = len(to) - 1

    # reverse edge: index = len(to) again
    to.append(u)
    cap.append(0)
    nxt.append(head[v])
    head[v] = len(to) - 1

# Read each of the m undirected roads and insert four directed arcs
for _ in range(m):
    u, v, c = map(int, input().split())
    add_edge(u, v, c)
    add_edge(v, u, c)

s, t = A, B

# Dinic's data structures
level = [-1] * (n + 1)
it    = [0]  * (n + 1)

def bfs() -> bool:
    """
    Builds the level graph via BFS from s.  
    Returns True if t is still reachable; False otherwise.
    """
    for i in range(1, n + 1):
        level[i] = -1

    dq = deque([s])
    level[s] = 0

    while dq:
        u = dq.popleft()
        e = head[u]
        while e != -1:
            v = to[e]
            if cap[e] > 0 and level[v] < 0:
                level[v] = level[u] + 1
                if v == t:
                    return True
                dq.append(v)
            e = nxt[e]
    return (level[t] >= 0)

def dfs(u: int, f: int) -> int:
    """
    Attempts to push up to f units of flow from node u to t along
    the level graph. Returns how much flow was actually pushed.
    """
    if u == t:
        return f

    e = it[u]
    while e != -1:
        v = to[e]
        # Only go “forward” if there is residual capacity and v is exactly one level deeper
        if cap[e] > 0 and level[v] == level[u] + 1:
            pushed = dfs(v, f if f < cap[e] else cap[e])
            if pushed > 0:
                cap[e]     -= pushed
                cap[e ^ 1] += pushed  # e^1 is the reverse edge
                return pushed
        e = nxt[e]
        it[u] = e

    return 0

flow = 0
while bfs():
    # Reset the “current‐edge” pointers for each node
    for i in range(1, n + 1):
        it[i] = head[i]
    # Keep digging blocking flow until none remains
    while True:
        pushed = dfs(s, INF)
        if pushed == 0:
            break
        flow += pushed

print(flow)
