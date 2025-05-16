"""
Understanding the Problem:

We are given a tree of n exhibits (nodes), where each exhibit is connected by a path (edge),
and there is exactly one path between any two exhibits (i.e a tree structure).
The task is to place a brochure booth at one of the exhibits such that 
the maximum time taken to reach any exhibit (i.e., the farthest one) is minimized.

This corresponds to finding the radius of the tree:
- The diameter of the tree is the longest path between any two nodes.
- The radius is the minimum possible maximum distance from any node to the rest, 
  which is ceil(diameter / 2).

Plan of Attack:
- Perform a BFS from an arbitrary node (say node 1) to find the farthest node u.
- From u, perform a second BFS to find the farthest node v and its distance d.
  This d is the diameter of the tree.
- The optimal placement for the brochure booth is at the center of the diameter path.
- The answer is ceil(d / 2), which gives the radius.

Time Complexity:
- BFS runs in O(n), and we perform it twice.
- Total time complexity: O(n)

This approach is efficient even for large trees (up to 1e5 nodes).

References:
1. https://cs.stackexchange.com/questions/22855/algorithm-to-find-diameter-of-a-tree-using-bfs-dfs-why-does-it-work
2. https://www.geeksforgeeks.org/graph-measurements-length-distance-diameter-eccentricity-radius-center/
3. https://www.youtube.com/watch?v=04x5aGu6Oew
"""


from collections import deque

n = int(input())
adj = [[] for _ in range(n+1)]


for _ in range(n-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def bfs(start):
    
    dist = [-1] * (n+1)
    dist[start] = 0
    q = deque([start])
    
    far_node = start
    maxd = 0
    
    while q:
        u = q.popleft()
        for w in adj[u]:
            
            if dist[w] == -1:
                dist[w] = dist[u] + 1
                
                q.append(w)
                
                
                if dist[w] > maxd:
                    
                    maxd = dist[w]
                    far_node = w
    
    
    return far_node, maxd

# BFS from node 1 to find one endpoint u of the diameter
u, _ = bfs(1)


# BFS from u to find the diameter length d
_, dia = bfs(u)

# radius
print((dia + 1) // 2)
