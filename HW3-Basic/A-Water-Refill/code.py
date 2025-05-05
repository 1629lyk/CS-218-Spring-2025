"""
Algorithm Explanation:

So we have 'n' students (jobs) and 'm' faucets (machines), 
we want to get everyone to finish as fast as possible.

The most optimal way to do this is if we can give the next student to the faucet that becomes free the earliest.
From this, no faucet stays waiting for too long, and the work is shared as evenly as possible.

Min-heap keeps track of when each faucet will be free.

At first, we send the first 'm' students to fill water at the faucets and put their finishing times into the heap.
After that, for every new student, we take out the faucet that becomes free the earliest,
assign the new student to it, and update the heap with the new finishing time.
So once all the students are done, the largest time in the heap tells us how long it took for everyone to finish.

Time Complexity:
1. Initial heap construction with 'm' elements: O(m)
2. For each of the remaining 'n - m' students:
   - Extract-min operation: O(log m)
   - Insert operation: O(log m)
   Total for 'n - m' students: O((n - m) * log m)
   
Overall Time Complexity: O(n log m)

References:
1. https://www.geeksforgeeks.org/job-sequencing-problem/
2. https://en.wikipedia.org/wiki/List_scheduling
"""


import heapq

n, m = map(int, input().split())
w = list(map(int, input().split()))

# First m students occupy the faucets
pq = w[:m]
heapq.heapify(pq)

# Take care of remaining students
for i in range(m, n):
    t = heapq.heappop(pq)
    heapq.heappush(pq, t + w[i])

res = max(pq)
print(res)
