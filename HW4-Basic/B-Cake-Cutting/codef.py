"""
Understanding the Problem:

A circular cake is divided into n slices of varying sizes.
Two players, Preston and Celvin, take turns picking slices.
- Preston picks first and aims to maximize the total size of slices he eats.
- Celvin plays greedily, always choosing the largest available slice adjacent to a taken one.
Only slices adjacent to already-taken ones can be picked.

The challenge is to determine the best starting slice for Preston
so that the total amount of cake he eats is maximized,
considering Celvin will always respond greedily.

Plan of Attack:
- Convert the circular problem to a linear one by duplicating the array (A * 2).
- Apply interval dynamic programming (DP) on all length-n subarrays.
- Let dp[i][j] be the maximum cake Preston can collect from interval [i, j]
  if both players play optimally (Preston optimizes, Celvin plays greedily).
- For each interval:
    - If Preston takes the left end (A[i]), Celvin picks either A[i+1] or A[j] greedily.
    - If Preston takes the right end (A[j]), Celvin picks either A[i] or A[j-1] greedily.
    - Update dp[i][j] using the best outcome of the two choices.

- After filling the dp table, consider all n-length windows from the 2n-length array
  and return the maximum value as the final answer.

Time Complexity:
- Outer loop over lengths up to n: O(n)
- Inner loop over 2n elements: O(n)
- Each dp[i][j] is computed in constant time.

Overall Time Complexity: O(n^2)

References:
https://www.atlantis-press.com/article/125968563.pdf
"""


def max_cake_preston_can_get(n, A):
    A = A * 2  
    
    dp = [[0] * (2 * n) for _ in range(2 * n)]
    
    
    prefix = [0] * (2 * n + 1)

    for i in range(2 * n):
        prefix[i + 1] = prefix[i] + A[i]
        dp[i][i] = A[i]

    
    for length in range(2, n + 1):
        for i in range(2 * n - length + 1):
            j = i + length - 1
    
            # If Preston takes left
            left_val = A[i]
            if A[i + 1] > A[j]:
                if i + 2 <= j:
                    left_score = left_val + dp[i + 2][j]
                else:
                    left_score = left_val
            else:
                if i + 1 <= j - 1:
                    left_score = left_val + dp[i + 1][j - 1]
                else:
                    left_score = left_val

            # If Preston takes right
            right_val = A[j]
            if A[i] > A[j - 1]:
                if i + 1 <= j - 1:
                    right_score = right_val + dp[i + 1][j - 1]
                else:
                    right_score = right_val
            else:
                if i <= j - 2:
                    right_score = right_val + dp[i][j - 2]
                else:
                    right_score = right_val

            dp[i][j] = max(left_score, right_score)

    # Consider all length-n intervals
    best = 0
    for i in range(n):
        best = max(best, dp[i][i + n - 1])
    return best



n = int(input())

A = []
for _ in range(n):
    A.append(int(input()))


print(max_cake_preston_can_get(n, A))
