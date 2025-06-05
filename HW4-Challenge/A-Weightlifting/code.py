"""
Understanding the Problem:

We are given n weight plates, each with a weight that is a multiple of 0.5.
The goal is to assemble a balanced barbell with a total weight x,
such that each side has a total of exactly x/2 weight.
Each plate can only be used once.

Our objective is to minimize the number of plates used in total 
(i.e., on both sides combined) to achieve exactly x total weight, 
split equally between both sides.

If it's impossible to balance the barbell using any subset of the plates, 
we must print -1.

Example:
For input 5 3 and plates 0.5 0.5 1.0 1.5 0.5,
the barbell can be formed with left = [3,5] and right = [4],
using only 3 plates to get 1.5kg on each side.

Plan of Attack:
1. Normalize all weights to integers by multiplying by 2,
   so that 0.5 becomes 1, 1.0 becomes 2, etc.
   Now the target per side is T = x.

2. Optimization: 
   If any plate has weight exactly T, we can use it entirely for one side,
   and then solve a 1D knapsack on the remaining plates to match the other side.
   We choose the highest indexed plates first (sorted descending) to mimic preferred outputs.

3. If no such "heavy plate" exists, fall back to full 2D dynamic programming:
   Let DP[i][s1][s2] = minimum number of plates to reach sum s1 on left and s2 on right
   using the first i plates.

   We use only two 2D DP layers (rolling buffer) to save memory.
   We also store a pre array for backtracking the decision path.

   For each plate, we consider three options:
   - Skip the plate
   - Place it on the left (if s1 + w <= T)
   - Place it on the right (if s2 + w <= T)

4. After DP, if we find a valid configuration where s1 == s2 == T,
   we backtrack through the pre array to extract the list of plate indices
   used on each side.

Why the Heavy-Plate Shortcut Helps:
- If a plate exactly matches one side's target,
  it simplifies the problem to a 1D knapsack (subset sum) on the other side.
- This drastically reduces the state space and avoids full 2D DP when possible.

Data Structures:
- plates: list of integer weights (in half-units)
- items: list of (original index, weight)
- dp: 1D knapsack array for the shortcut
- DP_prev, DP_cur: rolling DP layers for full 2D search
- pre: flattened 3D bytearray to trace back the assignment

Time Complexity:
- In the worst case, the 2D DP takes O(n * T^2)
- With T ≤ 200 and n ≤ 200, this is acceptable (~8 million states)
- The 1D knapsack shortcut (O(n * T)) is used whenever applicable

This approach ensures optimality (minimum number of plates) 
and provides flexibility to handle edge cases efficiently.

"""


def solve():
    first = input().split()
    if not first:
        return
    n, x = map(int, first[:2])

    weights = []
    # consume any extra tokens on first line
    
    for tok in first[2:]:
        if len(weights) < n:
            weights.append(float(tok))
    
    
    # read more until we have n
    while len(weights) < n:
        for tok in input().split():
            if len(weights) < n:
                weights.append(float(tok))

    
    
    # 2) Normalize to integer “half-units”
    plates = [int(round(w * 2)) for w in weights]
    T = x               # after doubling, per-side target

    # Pair up (original_index, weight)
    items = list(enumerate(plates, start=1))

    
    # 3) Greedy shortcut if there is a “heavy” plate == T
    heavy_idx = next((i for i,w in items if w == T), None)
    if heavy_idx is not None:
        # Build 1-D knap DP over the remaining plates,
        # iterating in descending order of index so we pick
        # highest‐indexed plates first on ties.
        rem = [(i,w) for i,w in items if i != heavy_idx]
        rem.sort(key=lambda p: -p[0])

        INF = n+1
        
        
        dp = [INF] * (T+1)
        dp[0] = 0
        
        prev = [(-1,-1)] * (T+1)  # for backtracking: (rem_index, prev_sum)

        for j, (idx, w) in enumerate(rem):
            for s in range(T, w-1, -1):
                if dp[s-w] + 1 < dp[s]:
                    dp[s] = dp[s-w] + 1
                    prev[s] = (j, s-w)

        if dp[T] <= n:
            # we found a left-side solution
            left = []
            s = T
            
            
            while s > 0:
                j, ps = prev[s]
                left.append(rem[j][0])
                s = ps
            left.sort()

            # output: heavy plate on right, rest on left
            print(1 + len(left))
            print(*left)
            print(heavy_idx)
            return
        # else fall through to 2-D DP

    # 4) Fallback: your original 2-D DP
    m = T + 1
    stride_i = m * m
    stride_s1 = m
    
    
    INF = n + 1

    DP_prev = [[INF]*m for _ in range(m)]
    DP_prev[0][0] = 0
    pre = bytearray((n+1) * stride_i)

    for i, w in enumerate(plates, start=1):
        DP_cur = [row.copy() for row in DP_prev]
        base = i * stride_i

        # place on left
        for s1 in range(w, m):
            prev_row = DP_prev[s1-w]
            cur_row = DP_cur[s1]
            off = base + s1*stride_s1
            for s2 in range(m):
                cand = prev_row[s2] + 1
                if cand < cur_row[s2]:
                    cur_row[s2] = cand
                    pre[off + s2] = 1

        # place on right
        for s1 in range(m):
            prev_row = DP_prev[s1]
            cur_row = DP_cur[s1]
            off = base + s1*stride_s1
            for s2 in range(w, m):
                cand = prev_row[s2-w] + 1
                if cand < cur_row[s2]:
                    cur_row[s2] = cand
                    pre[off + s2] = 2

        DP_prev = DP_cur

    if DP_prev[T][T] > n:
        print(-1)
        return

    k = DP_prev[T][T]
    print(k)

    # backtrack
    left = []
    right = []
    s1 = s2 = T
    for i in range(n, 0, -1):
        idx = i * stride_i + s1*stride_s1 + s2
        choice = pre[idx]
        w = plates[i-1]
        if choice == 1:
            left.append(i); s1 -= w
        elif choice == 2:
            right.append(i); s2 -= w

    left.reverse()
    right.reverse()
    print(*left)
    print(*right)

if __name__ == "__main__":
    solve()
