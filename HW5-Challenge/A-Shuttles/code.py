"""
Understanding the Problem:

We are given a list of subway stations and Olympic event venues, 
each represented by their 2D coordinates. 
Shuttles will operate between a venue and any nearby station within a distance <= d.
Every such shuttle route must be supported by at least one charging station
placed at either end of the route (venue or station).

Goal:
Minimize the total number of charging stations such that every active shuttle
(i.e., every edge between a station and a venue within distance d)
has at least one endpoint equipped with a charging station.

Modeling as a Graph Problem:

- We treat the problem as a bipartite graph:
    * Left set: Subway stations (indices 0 to n-1)
    * Right set: Venues (indices 0 to m-1)
    * Edges: Connect a station i to a venue j if the Euclidean distance ≤ d.

- Now the challenge becomes:
    Place charging stations on the minimum number of nodes
    such that every edge has at least one endpoint with a charger.

Graph Theory Insight:

This is the classical Minimum Vertex Cover problem on a bipartite graph.
By König's Theorem, in a bipartite graph:
    - Size of the minimum vertex cover = Size of the maximum matching

Thus, the task reduces to finding the maximum number of disjoint edges 
(station <-> venue pairs) where no two edges share a node.

Algorithm:

We use a standard DFS-based augmenting path algorithm to compute 
a maximum matching in the bipartite graph.

Key Data Structures:

- adj[i]: adjacency list, holds all venue indices j such that station i and venue j are within distance d.
- matchR[j]: holds the station index currently matched to venue j. 
           If matchR[j] == -1, then venue j is unmatched.
- visited[j]: marks if venue j has already been visited in the current DFS.

Matching Logic:

- For each station i (on the left), we attempt to find an augmenting path:
    * Try each adjacent venue j:
        - If j is unmatched, match it to i.
        - If j is matched to some other station, recursively try to find another match for that station.
- If a match is found, increment the result.

Why This Works:

- The number of successful matches = size of the maximum matching
- By König's theorem, this number is also the minimum number of charging stations needed.

Time Complexity:

- Each DFS traversal takes O(m) time in the worst case.
- Total time complexity is O(n * m), which is acceptable for n, m <= 100.

This approach is optimal, correct, and handles all edge cases gracefully.

References:
1. https://en.wikipedia.org/wiki/K%C5%91nig%27s_theorem_(graph_theory)
2. https://cp-algorithms.com/graph/edmonds_karp.html 
3. https://www.geeksforgeeks.org/maximum-bipartite-matching/ 

"""

import sys

def dfs(u):
    
    for v in adj[u]:
        if not visited[v]:
            visited[v] = True
            
            # If venue v is free, or we can re-route the station currently matched to v:
            if matchR[v] == -1 or dfs(matchR[v]):
                
                matchR[v] = u
                return True
    
    return False


n, m, d = list(map(int, sys.stdin.readline().split()))

stations = []
for _ in range(n):
    x, y = list(map(int, sys.stdin.readline().split()))
    stations.append((x, y))

venues = []
for _ in range(m):
    x, y = list(map(int, sys.stdin.readline().split()))
    venues.append((x, y))

# Build adjacency: for each station i, list all venues j within distance <= d
d2 = d * d

adj = [[] for _ in range(n)]

for i in range(n):
    x1, y1 = stations[i]
    
    
    for j in range(m):
        x2, y2 = venues[j]
        dx = x1 - x2
        dy = y1 - y2
        
        if (dx * dx) + (dy * dy) <= d2:
            adj[i].append(j)


matchR = [-1] * m
result = 0

for i in range(n):
    visited = [False] * m
    if dfs(i):
        result += 1


print(result)