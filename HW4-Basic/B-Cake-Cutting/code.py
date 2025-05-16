import sys
input = sys.stdin.readline


n = int(input())

if n == 1:
    print("Insufficient")
    exit(0)


A = []
for _ in range(n):
    A.append(int(input()))


M = 2 * n


# dp_even = dp for all even segment‐lengths (0,2,4,...)
dp_even = [0] * (M + 1)   

# dp_odd  = dp for all odd  segment‐lengths (1,3,5,...)
# Unroll circle twice
B = A + A
dp_odd  = B[:]            # dp[1][i] = B[i] for i=0..M-1
# Build DP for lengths 2..n-1
for length in range(2, n):
    prev2 = dp_even if (length % 2 == 0) else dp_odd
    new_dp = [0] * (M - length + 1)
    # for each start i of a segment of this length:
    for i in range(M - length + 1):
        j = i + length - 1
        # If Preston takes left end
        if B[i+1] > B[j]:
            take_left = B[i] + prev2[i+2]
        else:
            take_left = B[i] + prev2[i+1]
        # If Preston takes right end
        if B[i] > B[j-1]:
            take_right = B[j] + prev2[i+1]
        else:
            take_right = B[j] + prev2[i]
        new_dp[i] = take_left if take_left > take_right else take_right
    if length % 2 == 0:
        dp_even = new_dp
    else:
        dp_odd = new_dp
# We need dp for segments of length n-2 (to evaluate Celvin's first move)
# n-2 is even precisely when n is even.
dp_n2 = dp_even if (n % 2 == 0) else dp_odd
ans = 0
# Try each initial pick i = 0..n-1
for i in range(n):
    left  = i + 1
    right = i + n - 1
    # Celvin moves first on segment [left..right] of length n-1
    if B[left] > B[right]:
        future = dp_n2[left+1]
    else:
        future = dp_n2[left]
    total = A[i] + future
    if total > ans:
        ans = total
print(ans)

