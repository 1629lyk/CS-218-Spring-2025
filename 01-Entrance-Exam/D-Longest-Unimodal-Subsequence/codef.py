"""
references:
https://youtu.be/aPQY__2H3tE?si=RaEgBRqVYgzPgNDz
"""

def l_unimodal_subseq(arr):
    n = len(arr)

    if n < 3:
        return 0

    # Longest Increasing Subsequence
    lis = [1] * n 
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                lis[i] = max(lis[i], lis[j] + 1) 

    # Longest Decreasing Subsequence 
    lds = [1] * n
    for i in reversed(range(n)):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                lds[i] = max(lds[i], lds[j] + 1) 


    max_u_seq = 0
    for i in range(n):
        if lis[i] > 1 and lds[i] > 1:
            max_u_seq = max(max_u_seq, lis[i] + lds[i] - 1) # for peak is counted -1 in both LIS and LDS

    return max_u_seq

def main():
    try:
        n = int(input())
        arr = list(map(int, input().split()))

        if len(arr) != n:
            raise ValueError("No match n")

        if not (1 <= n <= 1000):
            raise ValueError("must be 1 <= n <= 1000")

        # given range 10^6 in question
        for num in arr:
            if not (0 <= num <= 10**6):
                raise ValueError("Not in range acc question")

        print(l_unimodal_subseq(arr))

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()
