"""
Understanding the Problem:

We are given a classroom of students arranged in a grid of size r x c.
Each student has a shyness level between 1 and 200, and will only talk
to an adjacent student (up/down/left/right) if given candies ≥ their shyness.

Yihan wants to make sure that any announcement reaches every student,
which is only possible if the entire classroom becomes one connected group
through a sequence of friendships (edges between adjacent students).

The goal is to minimize the total number of candies given while still
ensuring the classroom is fully connected.

Key Insight:
- This is a Minimum Spanning Tree (MST) problem over a grid.
- Each edge between two adjacent students has a weight of
      w(u,v) = min(shyness[u], shyness[v]),
  because the student with the smaller shyness can be convinced
  to initiate the conversation, forming a bidirectional friendship.

Plan of Attack:
- Flatten the grid into a 1D array (0 to r * c - 1).
- For each cell, generate edges to its right and bottom neighbors
      (to avoid duplicates).
- Store all edges in "buckets" based on their weights (0 to 200).
- Use Kruskal's algorithm:
    - Iterate weights from 0 to 200.
    - For each edge of current weight, try to union the nodes.
    - If union is successful (i.e., connects two components), 
      add the weight to the total candy count.

Why Kruskal Works:
- By processing edges in order of increasing weight,
  we guarantee that we build the MST with minimum total cost.
- The DSU (Disjoint Set Union) ensures that we only add edges
  that actually help connect previously disconnected parts of the graph.

DSU Details:
- Each node starts in its own set.
- We use path compression in 'find' to speed up future lookups.
- We use union by size in 'union' to keep trees shallow and efficient.

Edge Bucketing:
- We bucket edges by weight so we can avoid explicit sorting.
- Since weights are integers between 1 and 200, this gives us
  an O(N + E) alternative to using a priority queue.

Time Complexity:
- Reading the grid: O(r * c)
- Building buckets: O(r * c)
- Processing edges with DSU: nearly O(N), where N = r * c
- Total runtime is efficient enough for N up to 10^6.

This approach ensures correctness, speed, and is well-suited for large grids.

References:
1. Kruskal's Algorithm: 
    a. Prof Yan Gu Slides: 18-Graph
    b. https://cp-algorithms.com/graph/mst_kruskal.html
2. Disjoint Set Union (DSU): https://cp-algorithms.com/data_structures/disjoint_set_union.html
"""



import sys
input = sys.stdin.readline

def find(p, x):
    while p[x] >= 0:
        if p[p[x]] >= 0:
            p[x] = p[p[x]]
        
        
        x = p[x]
    
    return x

def union(p, a, b):
    a, b = find(p, a), find(p, b)
    if a == b:
        return False
    
    if p[a] > p[b]:
        a, b = b, a
    
    
    p[a] += p[b]
    p[b] = a
    
    
    return True


r, c = map(int, input().split())
N = r * c
grid = []

for _ in range(r):
    grid.extend(map(int, input().split()))


# The shyness is a positive integer within 200.
buckets = [[] for _ in range(201)]


for i in range(r):
    for j in range(c):
        
        u = i * c + j
        su = grid[u]
        
        if i+1 < r:
            v = u + c
            buckets[min(su, grid[v])].append((u, v))
        
        
        if j+1 < c:
            v = u + 1
            buckets[min(su, grid[v])].append((u, v))


parent = [-1] * N

total = 0

for w in range(201):
    for u, v in buckets[w]:


        if union(parent, u, v):
            total += w
print(total)