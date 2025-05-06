"""
Understanding the Problem:

The task is to compute the minimum number of editing mistakes needed 
to turn Raj's answers into Sheldon's standard answers. 
The allowed operations (each costing 1) are:
- insertion (adding a letter),
- deletion (removing a letter).
- substitution (changing one letter into another),

This is a classic string problem known as the Levenshtein Distance

Plan of Attack:
- Use a modified version of Myers' algorithm for edit distance.
- The idea is to track, for each edit distance d from 0 up to 100,
  the furthest position in the string `s` (Raj's) that can be reached
  with at most `d` operations on diagonals `k = i - j` (i.e., alignment difference).
- At each step `d`, iterate over all diagonals `k` in the range [-d, d]:
  - Try extending from three possibilities:
    1. Deletion: move right in s only.
    2. Insertion: move down in t only.
    3. Substitution: move diagonally in both s and t.
  - From the chosen move, "snake" forward as long as characters match.
- The process continues until we reach the end of both strings.

Time Complexity:
- The algorithm runs in O(D * (N + M)), where D is the maximum edit distance (≤100),
  and N, M are the lengths of the input strings (≤100,000).
- In practice, it's linear in input size due to the small D.

Overall Time Complexity: O(D * n), where D ≤ 100.

References:
1. https://en.wikipedia.org/wiki/Levenshtein_distance
2. https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm

Self Note:
Given n can be up to 100,000, a naive dynamic programming 
approach with O(n^2) complexity would be too slow. 
Luckily, the problem guarantees that the number of edits needed 
is at most 100. This enables us to use a much faster algorithm.
"""


n = int(input())
s = input().strip()
t = input().strip()


if s == t:
    print(0)
    exit()

max_mis = 100
offset = max_mis
size = 2*max_mis + 1


N, M = len(s), len(t)

# furthest x  can reach on diagonal k = x-y with le d
V_old = [-1] * size

x0 = 0


while x0 < N and x0 < M and s[x0] == t[x0]:
    x0 += 1
V_old[offset] = x0


if x0 >= N and x0 >= M:
    print(0)
    exit()


for d in range(1, max_mis + 1):
    V = [-1] * size

    # consider all k from -d to +d in steps of 2
    for k in range(-d, d + 1):
        idx = k + offset
        best = -1

        # Check 1 deletion (move i by +1): from k-1 diagonal
        if -(d-1) <= k-1 <= (d-1):
            prev = V_old[(k-1) + offset]
            if prev >= 0:
                best = prev + 1

        # Check 2 insertion (move j by +1): from k+1 diagonal
        if -(d-1) <= k+1 <= (d-1):
            prev = V_old[(k+1) + offset]
            if prev >= 0 and prev > best:
                best = prev

        # Check 3 substitution (move both i and j by +1) at cost 1
        if -(d-1) <= k <= (d-1):
            prev = V_old[k + offset]
            if prev >= 0 and prev + 1 > best:
                best = prev + 1

        # for unreachable, skip
        if best < 0:
            continue

        
        x = best
        y = x - k
        
        
        while x < N and y < M and s[x] == t[y]:
            x += 1
            y += 1

        V[idx] = x

        
        if x >= N and y >= M:
            print(d)
            exit()

    V_old = V


print(max_mis)
