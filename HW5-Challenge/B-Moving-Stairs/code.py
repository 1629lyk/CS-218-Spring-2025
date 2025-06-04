"""
Understanding the Problem:

We are given a graph of platforms in Hogwarts, connected by magical stairways.
Each stairway connects a fixed platform x to two other platforms y and z, depending on time parity:
- At EVEN timestamps (0, 2, 4, ...), the stair connects x <-> y
- At ODD timestamps (1, 3, 5, ...), the stair connects x <-> z

Harry can:
- Wait on the same platform, costing 1 unit of time and toggling time parity.
- Use a stairway from his current platform, if it is one of the endpoints active at current time.
  After boarding, he travels for exactly 1 minute and ends up at the platform connected after the stair flips.

Goal:
Starting at platform 0 at time = 0, find the minimum time to reach a target platform k.

Approach:
We model this as a state-space search using 0-1 BFS.
Each state is defined by:
- Platform u
- Parity p (0 = even time, 1 = odd time)
We maintain a 2D distance array:
- dist[p][u] = shortest time to reach platform u at time parity p

Data Structures:
- stairs: List of (x, y, z) tuples for all stairways.
- adj: For each platform, a list of stair indices that touch it.
- dist: 2D array storing shortest known times for each (platform, parity).
- deque: Used for standard BFS to explore shortest paths.

BFS Exploration:
At each state (u, p), we explore:
1. Waiting on platform u:
   - Simply enqueue (u, 1-p) with time t+1 if not visited.

2. Riding a stair from u:
   - At even times (p == 0), stair (x,y,z) connects x <-> y:
       - From x: you can ride to z at t+1
       - From y: you can ride to x (current edge) and to z (after flip)
   - At odd times (p == 1), stair (x,y,z) connects x <-> z:
       - From x: you can ride to y at t+1
       - From z: you can ride to x (current edge) and to y (after flip)

Time and Space Complexity:
- Time: O(n + m), as each state is visited at most once and stairways are scanned per node.
- Space: O(n + m), due to adjacency list and distance table.

References:
1. https://www.youtube.com/watch?v=G_j14xj-zGc
2. https://cs.stackexchange.com/questions/168416/shortest-path-between-two-nodes-with-time-dependent-edge-weights
"""


from collections import deque

n, m, k = map(int, input().split())
idx = 3

# store every stair once
stairs = []
adj = [[] for _ in range(n)]          

for i in range(m):
    x, y, z = map(int, input().split())
    idx += 3
    stairs.append((x, y, z))
    adj[x].append(i)
    adj[y].append(i)
    adj[z].append(i)                  

INF = 10 ** 18
dist = [[INF] * n for _ in range(2)]  
dist[0][0] = 0

q = deque([(0, 0)])  

while q:
    u, p = q.popleft()
    t = dist[p][u]

    # option 1: wait
    if dist[1 - p][u] == INF:
        dist[1 - p][u] = t + 1
        q.append((u, 1 - p))

    # option 2: ride any stair touching u
    for sid in adj[u]:
        x, y, z = stairs[sid]

        
        # even minute, stair joins x-y
        
        if p == 0:  
            if u == x:
                v = z
                
                # x -> z
                if dist[1][v] == INF:
                    dist[1][v] = t + 1
                    q.append((v, 1))
            
            # y -> x and y -> z
            elif u == y:                  
                
                # to x
                if dist[1][x] == INF:
                    dist[1][x] = t + 1
                    q.append((x, 1))
                
                # to z
                if dist[1][z] == INF:
                    dist[1][z] = t + 1
                    q.append((z, 1))


        # p == 1, odd minute, stair joins x-z
        else:
            if u == x:
                v = y                     
                if dist[0][v] == INF:
                    dist[0][v] = t + 1
                    q.append((v, 0))
            elif u == z:                  

                if dist[0][x] == INF:
                    dist[0][x] = t + 1
                    q.append((x, 0))

                if dist[0][y] == INF:
                    dist[0][y] = t + 1
                    q.append((y, 0))

ans = min(dist[0][k], dist[1][k])
print(-1 if ans == INF else ans)