"""
References:
https://www.geeksforgeeks.org/puzzle-sitting-arrangement/

Algorithm Explanation:

A person is only happy when they sit next to a family member  in a pair or singles in a row.
We go through over all possible numbers of family pairs (x) that can be seated in r rows.
For each x, we check the leftover people and remaining rows.
Then check how many singles can be seated alone rather than sitting with a different family which breaks the rule.
The result is the maximum total number of happy people on all possibilities and combinations.

Time Complexity:
For each test case, we loop up to O(r) (maximum rows), which is at most 500.
Preprocessing steps like summing array elements take O(n), where n ≤ 100.

Complexity per test case is O(n)
So the overall time complexity per test case is O(r), and for t test cases, it's O(t * r).

"""

def max_happy_people(r, a):
    total = sum(a)
    pairs_count = sum(x // 2 for x in a)

    possi = 0
    max_x = min(pairs_count, total // 2, r)

    for x in range(max_x + 1):
        leftover = total - 2 * x
        leftover_rows = r - x

        # lgoic for singles seats
        if leftover <= 2 * leftover_rows:
            sin = min(leftover, leftover_rows, 2 * leftover_rows - leftover)
            sin = max(0, sin)
            current_happy = 2 * x + sin
            possi = max(possi, current_happy)

    return possi

def main():
    inp = int(input())
    for _ in range(inp):
        n, r = map(int, input().split())
        a = list(map(int, input().split()))
        result = max_happy_people(r, a)
        print(result)

if __name__ == "__main__":
    main()
