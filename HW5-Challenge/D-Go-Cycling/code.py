"""
Understanding the Problem:

We are given an n x m grid of integers, where each cell represents a height. 
Yan can move *only* downhill from a cell to one of its four neighbors 
(up, down, left, right) if the height of the neighbor is strictly less.

Every cell in the *top row* acts as an entrance and costs one ticket 
to enter. Once bought, that ticket can be reused for the same entrance. 
Every cell in the *bottom row* is an exit. If Yan reaches an exit, he can 
teleport back to any entrance for free.

The goal is to:
1. Determine whether it's possible to reach *all* bottom-row cells 
   using any combination of top-row entrances.
2. If so, find the *minimum number of entrance tickets* Yan needs 
   to buy to make all exits reachable.

Constraints: 
- The grid size can go up to 2000 x 2000, requiring an efficient O(nm log nm) approach.
- Heights can be large (up to 10^9), so only comparisons—not value operations—are used.

Plan of Attack:

Step 1: Multi-source BFS
- Start BFS from all top-row cells (all entrances).
- Only move to neighboring cells that are strictly lower in height (downhill).
- Track which bottom-row columns are reachable.
- If not all m bottom columns are reachable, print:
    0, <reachable_count> and terminate early.

Step 2: Reverse-Dijkstra (Interval Propagation)
- For each bottom cell (which is trivially an exit), define its reachable interval as [j, j].
- Use a max-heap (priority queue) to propagate these intervals uphill, i.e., from lower to higher cells.
- A cell's reachable interval becomes the union of its downhill neighbors' intervals.
- The final result is: for each top-row cell (0, j), determine which contiguous range of bottom columns it can reach.

Step 3: Greedy Interval Cover
- From all top-row entrances, collect the intervals [L[j], R[j]] of exits they can reach.
- Sort the intervals by starting column.
- Use a greedy algorithm to choose the *minimum number of intervals* (i.e., entrances) that cover all bottom columns [0..m-1].
- This is the classic "minimum number of intervals to cover a range" problem.

Why Two Passes?
- The first BFS ensures we don't perform expensive Dijkstra-based propagation if some exits are unreachable.
- The second pass gives accurate per-entrance coverage needed to compute the minimal ticket count.

Efficiency:
- The BFS runs in O(nm), visiting each cell once.
- The reverse Dijkstra uses a max-heap and processes each cell at most a few times → O(nm log nm).
- The final greedy interval cover is O(m log m), since we have at most m intervals to sort and cover.

This separation of concerns ensures correctness and performance.

References:
1. https://cp-algorithms.com/graph/dijkstra.html (for heap-based propagation)
"""


import sys
import heapq
from collections import deque
 
 
n, m = map(int, input().split())
 

hflat = [0] * (n * m)
for i in range(n):
    row = list(map(int, input().split()))
    base = i * m
    for j in range(m):
        hflat[base + j] = row[j]
 

mm = m
nn = n
h = hflat
size = n * m
 
# Step 1: Multi‐source BFS from all top‐row cells to check exact coverage 
 
visited = [False] * size
dq = deque()
 
# Start from every entrance (0, j)
for j in range(m):
    idx0 = j  # flat index for (0,j)
    visited[idx0] = True
    dq.append(idx0)
 
while dq:
    idx0 = dq.popleft()
    i0 = idx0 // mm
    j0 = idx0 - i0 * mm
    h0 = h[idx0]
    
    
    # Up neighbor
    if i0 > 0:
        idx1 = idx0 - mm
        if not visited[idx1] and h0 > h[idx1]:
            visited[idx1] = True
            dq.append(idx1)
    
    
    # Down neighbor
    if i0 < nn - 1:
        idx1 = idx0 + mm
        if not visited[idx1] and h0 > h[idx1]:
            visited[idx1] = True
            dq.append(idx1)
    
    
    # Left neighbor
    if j0 > 0:
        idx1 = idx0 - 1
        if not visited[idx1] and h0 > h[idx1]:
            visited[idx1] = True
            dq.append(idx1)
    
    
    # Right neighbor
    if j0 < mm - 1:
        idx1 = idx0 + 1
        if not visited[idx1] and h0 > h[idx1]:
            visited[idx1] = True
            dq.append(idx1)
 

# Count how many distinct bottom‐row columns are reachable
reachable_count = 0
bottom_base = (n - 1) * m
for j in range(m):
    if visited[bottom_base + j]:
        reachable_count += 1
 
# If not all exits reachable, print “0” and the count, then exit
if reachable_count < m:
    print(0)
    print(reachable_count)
    sys.exit()
 
# Step 2: Compute exact [L, R] interval for each cell via reverse‐Dijkstra 
 
# Initialize intervals to “unreachable”
L = [m] * size
R = [-1] * size
 
# Max‐heap (store negative height) seeded with all bottom‐row cells
heap = []
for j in range(m):
    idx0 = bottom_base + j
    L[idx0] = j
    R[idx0] = j
    heapq.heappush(heap, (-h[idx0], idx0))
 
while heap:
    negh, idx0 = heapq.heappop(heap)
    cur_l = L[idx0]
    cur_r = R[idx0]
    
    # Skip if unreachable (shouldn’t happen for bottom seeds)
    if cur_l > cur_r:
        continue
    
    
    h0 = -negh
    i0 = idx0 // mm
    j0 = idx0 - i0 * mm
    
    
    # Up neighbor
    if i0 > 0:
        idx1 = idx0 - mm
        if h[idx1] > h0:
            nl = cur_l if cur_l < L[idx1] else L[idx1]
            nr = cur_r if cur_r > R[idx1] else R[idx1]
            if nl < L[idx1] or nr > R[idx1]:
                L[idx1] = nl
                R[idx1] = nr
                heapq.heappush(heap, (-h[idx1], idx1))
    
    
    # Down neighbor
    if i0 < nn - 1:
        idx1 = idx0 + mm
        if h[idx1] > h0:
            nl = cur_l if cur_l < L[idx1] else L[idx1]
            nr = cur_r if cur_r > R[idx1] else R[idx1]
            if nl < L[idx1] or nr > R[idx1]:
                L[idx1] = nl
                R[idx1] = nr
                heapq.heappush(heap, (-h[idx1], idx1))
    
    
    # Left neighbor
    if j0 > 0:
        idx1 = idx0 - 1
        if h[idx1] > h0:
            nl = cur_l if cur_l < L[idx1] else L[idx1]
            nr = cur_r if cur_r > R[idx1] else R[idx1]
            if nl < L[idx1] or nr > R[idx1]:
                L[idx1] = nl
                R[idx1] = nr
                heapq.heappush(heap, (-h[idx1], idx1))
    
    
    # Right neighbor
    if j0 < mm - 1:
        idx1 = idx0 + 1
        if h[idx1] > h0:
            nl = cur_l if cur_l < L[idx1] else L[idx1]
            nr = cur_r if cur_r > R[idx1] else R[idx1]
            if nl < L[idx1] or nr > R[idx1]:
                L[idx1] = nl
                R[idx1] = nr
                heapq.heappush(heap, (-h[idx1], idx1))
 
# Step 3: Gather intervals for each entrance and run greedy cover 
 
intervals = []
for j in range(m):
    idx0 = j  # flat index for (0,j)
    intervals.append((L[idx0], R[idx0]))

# Sort by left endpoint
intervals.sort(key=lambda x: x[0])
 
covered_up_to = -1
ans = 0
i = 0
best_r = -1
N = len(intervals)
 
while covered_up_to < m - 1:
    target = covered_up_to + 1
    while i < N and intervals[i][0] <= target:
        if intervals[i][1] > best_r:
            best_r = intervals[i][1]
        i += 1
    # Extend coverage by picking the interval that reaches best_r
    ans += 1
    covered_up_to = best_r
 
print(1)
print(ans)
