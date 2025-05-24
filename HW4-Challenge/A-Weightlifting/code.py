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

    # ——— 2) Normalize to integer “half-units” ———
    plates = [int(round(w * 2)) for w in weights]
    T = x               # after doubling, per-side target

    # Pair up (original_index, weight)
    items = list(enumerate(plates, start=1))

    # ——— 3) Greedy shortcut if there is a “heavy” plate == T ———
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

    # ——— 4) Fallback: your original 2-D DP ———
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
