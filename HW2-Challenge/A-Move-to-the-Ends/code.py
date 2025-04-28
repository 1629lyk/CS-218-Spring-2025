"""
The optimal way to minimize the number of moves is to preserve the longest subsequence
So we are allowed to move any element either to the beginning or to the end of the array.
where elements are consecutive in value and already in left-to-right order.
Thus, the elements forming a consecutive increasing sequence are left untouched,
and all other elements are moved either to the beginning or the end.

To find the largest such sequence:
- We iterate through the array once.
- For each element `v`, we calculate the length of the longest consecutive subsequence ending at `v`
  by using `seq_v[v] = seq_v.get(v-1, 0) + 1`.
- We track the maximum such sequence length (`longest`) found.

Finally, the minimum number of moves needed is (n - longest), 
where `n` is the total number of elements.

Time Complexity:
1. Single pass over array elements: O(n)
2. Hash map updates and lookups per element: O(1) amortized

Thus, overall time complexity: O(n) per test case.

References: 
1. https://www.geeksforgeeks.org/longest-increasing-consecutive-subsequence/
2. https://takeuforward.org/data-structure/longest-consecutive-sequence-in-an-array/
"""


t_case = int(input())
results = []

for _ in range(t_case):
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Compute minimum moves to sort the array using allowed operations
    seq_v = {}  # seq_v[v] = length of the longest consecutive subsequence ending at v
    longest = 0
    for v in arr:
        seq_v[v] = seq_v.get(v - 1, 0) + 1
        longest = max(longest, seq_v[v])
    
    results.append(str(n - longest))

print("\n".join(results))
