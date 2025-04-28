"""
The plan of attack is to ensure that every point on the 42,195m marathon track is covered
by at least two cameras using the minimum number of placements. 
Each camera has a pre-determined location and coverage radius.

The steps would be:
1. Place each camera's interval within [0, 42195] and discard any irrelevant ones.
2. Sort all valid intervals based on their left endpoints.
3. Sweep from the start of the track, maintaining two heaps:
   i. active min-heap for right ends of cameras already chosen.
   ii. cand max-heap for right ends of cameras that are visible but not yet chosen.
4. At each critical point (a camera's right endpoint), make sure that at least two cameras 
   cover the current position:
   i. Remove expired cameras whose coverage has ended.
   ii. Greedily select the next farthest-reaching camera when coverage falls below two.
5. Move the position pointer only to critical events where coverage may drop (camera expiry).

Time Complexity:
1. Sorting intervals: O(n log n)
2. Heap operations (push and pop) at most O(log n) each and O(n) total operations
Thus, overall time complexity: O(n log n) per test case.

References:
1. https://cs.stackexchange.com/questions/151112/greedy-algorithm-for-postive-interval-covering
2. https://www.geeksforgeeks.org/minimum-number-of-intervals-to-cover-the-target-interval/
3. https://dilipkumar.medium.com/sweep-line-algorithm-e1db4796d638
4. https://www.youtube.com/watch?v=YnIxejYW7cE
"""

import heapq

LENGTH = 42195



def clamp_and_sort(raw, length=LENGTH):
    #Yield (l, r) intervals clipped to the track and sorted by l.
    ivals = []
    
    for x, k in raw:
        l = max(0, x - k)
        r = min(length, x + k)
        
        if l <= r:
            ivals.append((l, r))
    
    ivals.sort() 
    return ivals



def min_double_cover(intervals, length=LENGTH):
    
    # Greedy, event-driven sweep.
    # Return the minimum camera count, or -1 if impossible.
    
    heap_cand   = [] # max-heap  (-r, r) of visible but not chosen
    heap_r = [] # min-heap: right ends of active cameras

    i   = 0 
    pos = 0 
    ans = 0 

    while pos < length:
        
        while i < len(intervals) and intervals[i][0] <= pos:
            heapq.heappush(heap_cand, (-intervals[i][1], intervals[i][1]))
            i += 1

        
        while heap_r and heap_r[0] < pos:
            heapq.heappop(heap_r)

        
        while len(heap_r) < 2:
            while heap_cand and heap_cand[0][1] < pos:     
                heapq.heappop(heap_cand)
            
            if not heap_cand:                        
                return -1
            
            # farthest-reaching
            r = heapq.heappop(heap_cand)[1]
            heapq.heappush(heap_r, r)
            ans += 1

        
        next_end = heap_r[0] 
        pos = next_end       

    
        while heap_r and heap_r[0] == next_end:
            heapq.heappop(heap_r)

    return ans



n = int(input().strip())
pairs = [tuple(map(int, input().split())) for _ in range(n)]

intervals = clamp_and_sort(pairs)          
print(min_double_cover(intervals))
