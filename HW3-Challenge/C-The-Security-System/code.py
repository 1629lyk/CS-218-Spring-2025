"""
Understanding the Problem:

A security system across an L * L apartment grid is simulated in this problem.
So each row sends a horizontal sensor signal to the right side of the room, and
each furniture piece blocks the signal on certain rows, represented by a vertical segment 

from (a, b) to (c, d), where b = d (fixed column).

The objective is to ensure no row has more than k furniture blocks on the path of the signal.
To achieve this, we may need to remove some furniture, and we want to minimize the number remd.

Plan of Attack:
    - Use a max-heap to store all active furniture segments keyed by their ending row (to prioritize longest ones).
    - For each row from 1 to L, maintain a count of "active" segments that intersect the row.
    - When a row exceeds the allowed count k, greedily remove the segment with the farthest ending row.
    - This greedy strategy ensures fewer future rows will be affected, minimizing total rems.
    - Track when segments start and end using two arrays (st[], en[]).
    - Only segments not already remd are counted towards "active".
    - At each row, clean up expired segments (those ending at this row).

Time Complexity:
    - Each of the n furniture segments is pushed and popped from the heap at most once.
    - Heap operations are O(log n), and we perform up to O(n) such operations.
    - Total complexity is O((n + L) log n), which is efficient for n, L le 10^5.

Overall Time Complexity: O((n + L) * log n)

References:
1. https://www.geeksforgeeks.org/minimum-rems-required-to-make-ranges-non-overlapping/
2. https://www.geeksforgeeks.org/how-to-implement-interval-scheduling-algorithm-in-python/
3. https://blog.heycoach.in/greedy-algorithm-for-interval-scheduling/
"""


import heapq

inp = input().split()

if not inp:
    exit()

L, n, k = map(int, inp)
st = [[] for _ in range(L+1)]
en = [[] for _ in range(L+1)]

heap = []   # store -c, i so that largest c is popped first
actv = 0
rems = 0

seg_end = [0]*n
for i in range(n):
    a, b, c, d = map(int, input().split())
    

    st[a].append(i)
    en[c].append(i)
    seg_end[i] = c


remd = [False]*n

for r in range(1, L+1):
    
    for i in st[r]:
        heapq.heappush(heap, (-seg_end[i], i))
        actv += 1
    
    # remove largest end first for too many actives
    while actv > k:
        negc, i = heapq.heappop(heap)

        
        if remd[i] or seg_end[i] < r:
            continue

        remd[i] = True
        rems += 1
        actv -= 1


    #  segments that end at r be remd
    for i in en[r]:
        if not remd[i]:
            actv -= 1


print(rems)