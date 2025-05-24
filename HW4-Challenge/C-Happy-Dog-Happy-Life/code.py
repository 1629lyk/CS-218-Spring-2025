"""
Understanding the Problem:

We are given a list of toys, each with a funness value.
A dog will only accept a new toy if its funness is strictly 
greater than any toy received before. On each day, the total 
"happiness" is the sum of funness values of all toys 
the dog currently owns.

The goal is to find the optimal (strictly increasing) 
sequence of toys to maximize the dog's total happiness across all days.

How is Happiness Calculated?
- If you give a toy with funness f[i] on day i, 
  the dog uses it from day i to day n (inclusive).
- So, toy i contributes f[i] * (n - i) to total happiness.
- This is the "weight" or value of picking toy i.

Key Observations:
- You can skip toys but must pick a strictly increasing sequence of funness.
- The problem reduces to finding a **weighted Longest Increasing Subsequence (LIS)** 
  where the weight of element i is f[i] * (n - i).

Plan of Attack:
1. Compute weights: f[i] * (n - i) for each toy.
2. Compress funness values to ensure we can use them as indices 
   in a Fenwick Tree (BIT) of size at most n.
3. Use dynamic programming with BIT:
   - At each toy i, query the max DP value among all previous 
     funnesses smaller than f[i].
   - Add the current toy's weight to that value.
   - Update the BIT to reflect the new max value for f[i].
   - Track the global maximum DP value.

Why Use a Fenwick Tree?
- To answer "maximum of all previous DP values with smaller funness" in O(log n).
- Allows efficient updates and queries within compressed funness indices.
- This is necessary to handle up to 10⁵ toys within time limits.

Time Complexity:
- Sorting and compression: O(n log n)
- Main loop: O(n log n) using BIT
- Total: O(n log n)

This ensures an optimal and scalable solution for large inputs.

References:
1. https://cp-algorithms.com/data_structures/fenwick.html
2. https://www.geeksforgeeks.org/fenwick-tree-for-competitive-programming/
3. https://stackoverflow.com/questions/8782943/maximum-weight-increasing-subsequence 
"""

n = int(input())
f = list(map(int, input().split()))


weights = []
for i in range(n):
    w = f[i] * (n - i)
    weights.append(w)


uniq = sorted(set(f))



comp = {}
for idx, v in enumerate(uniq):
    comp[v] = idx + 1 

m = len(uniq)


bit = [0] * (m + 1)
answer = 0



def bit_update(bit, size, i, val):
    # point-update: set bit[i] = max(bit[i], val)
    while i <= size:
        if bit[i] < val:
            bit[i] = val
        i += i & -i

def bit_query(bit, i):
    res = 0
    while i > 0:
        if bit[i] > res:
            res = bit[i]
        i -= i & -i
    return res


# DP -> for each toy i, find best previous DP for smaller funness
for i in range(n):
    idx = comp[f[i]]
  
    best_prev = bit_query(bit, idx - 1)
    dp_i = best_prev + weights[i]
  
    bit_update(bit, m, idx, dp_i)
  
  
    if dp_i > answer:
        answer = dp_i



print(answer)