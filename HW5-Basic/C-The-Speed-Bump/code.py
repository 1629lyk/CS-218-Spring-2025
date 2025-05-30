"""
Understanding the Problem:

We are given a road map of a city as a weighted undirected graph,
where each road has two attributes:
    - Number of speed bumps on the road (c)
    - Length/distance of the road (d)

Sheldon wants to travel from home (node 0) to university (node n-1).
He wants to:
1. Minimize the total number of speed bumps along the route.
2. If multiple routes have the same number of bumps, pick the one with the shortest distance.

Thus, we need to find a path from node 0 to node n-1 that:
- Minimizes (total_bumps, total_distance) lexicographically.

Why Dijkstra's Algorithm Works Here:
- Dijkstra's algorithm is used to find the shortest path in graphs with non-negative weights.
- In our case, the "distance" metric is replaced with a pair (bumps, distance).
- We extend Dijkstra by using this pair as the key in the min-heap (priority queue).

Plan of Attack:
- Build the graph as an adjacency list from the input roads.
- Initialize a dist array where dist[u] = (min_bumps, min_length) to reach node u.
- Use a min-heap to always expand the node with the smallest (bumps, distance).
- For each neighbor of the current node, calculate the new (bumps, distance).
- If the new pair is strictly better than the current stored value, update and push it.

Why Lexicographic Comparison:
- Python's tuple comparison naturally works lexicographically:
    - (a1, b1) < (a2, b2) if (a1 < a2) or (a1 == a2 and b1 < b2)
- So we can directly store (bumps, distance) in both the dist array and heap.

Time and Space Complexity:
- Time: O((n + m) log n), where n = number of nodes, m = number of edges.
- Space: O(n + m) for graph and distance arrays.

This solution ensures:
- Correctness even with large inputs (n up to 1e5, m up to 2e5)
- Efficient route computation using minimal bumps and shortest distance.

References:
1. https://cp-algorithms.com/graph/dijkstra.html
2. https://stackoverflow.com/questions/22897209/how-to-use-tuples-in-dijkstras-algorithm
"""



import heapq
INF = 10**18

inp_l = input().split()
n, m = map(int, inp_l)


graph = [[] for _ in range(n)]


for _ in range(m):
    a, b, c, d = map(int, input().split())
    graph[a].append((b, c, d))
    graph[b].append((a, c, d))



dist = [(INF, INF)] * n
dist[0] = (0, 0)


heap = [(0, 0, 0)]

while heap:
    bumps_u, len_u, u = heapq.heappop(heap)

    if (bumps_u, len_u) > dist[u]:
        continue

    for v, cb, db in graph[u]:

        new_bumps = bumps_u + cb
        new_len = len_u + db


        if (new_bumps, new_len) < dist[v]:
            dist[v] = (new_bumps, new_len)


            heapq.heappush(heap, (new_bumps, new_len, v))


ans_bumps, ans_len = dist[n-1]


print(ans_bumps, ans_len)

