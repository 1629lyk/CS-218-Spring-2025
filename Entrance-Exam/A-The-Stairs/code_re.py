def find_special_step():
    n = int(input().strip())
    a = [int(input().strip()) for _ in range(n)]

    # Count frequencies of consecutive differences
    diff_counts = {}
    for i in range(1, n):
        d = a[i] - a[i - 1]
        diff_counts[d] = diff_counts.get(d, 0) + 1

    # The correct step‐to‐step difference is the one that appears most often
    true_d = max(diff_counts, key=diff_counts.get)

    # Try each index x (0-based) as the “wrong” step
    for x in range(n):
        if x == 0:
            # If step 0 is wrong, assume step 1 and onwards follow the correct difference
            base = a[1] - true_d
        else:
            # Otherwise, assume the sequence starts correctly at a[0]
            base = a[0]

        ok = True
        for i in range(n):
            if i == x:
                continue
            expected = base + i * true_d
            if a[i] != expected:
                ok = False
                break

        if ok:
            # Output the 1-based index of the altered step
            print(x + 1)
            return

if __name__ == "__main__":
    find_special_step()
