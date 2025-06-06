"""
References:
1. https://www.geeksforgeeks.org/when-should-i-use-two-pointer-approach/
2. https://www.geeksforgeeks.org/introduction-to-greedy-algorithm-data-structures-and-algorithm-tutorials/

Algorithm Explanation:
The plan is to form the max number of swimming trios groups consisting of
1 male and 2 females, and the condition is that the  male is always taller than both selected females.
first we should sort both male and female height arrays.
Then, using a greedy two-pointer approach, we iterate over each male and
try to find the smallest pair of vacant females who are both shorter than the male that is selected.
If found, make and increment the count of the trio and move the female pointer forward by 2 as 2 females are selected.
This shows that pairing is done for shortest compatible females first


Time Complexity:
Sorting both arrays takes O(n log n + m log m), where n and m are the number of females and males.
For the greedy two-pointer scan, it takes O(n + m).
The overall time complexity is O(n log n + m log m).
"""
def max_pairs(n, m, males, females):
    # males.sort(reverse=True)
    males.sort()
    females.sort()

    i = j = tri_grps = 0

    while i < n and j + 1 < m:
        if females[j] < males[i] and females[j + 1] < males[i]:
            tri_grps += 1
            j += 2
        i += 1

    return tri_grps


def main():
    n, m = map(int, input().split()) # n -> females, m -> males all count of
    males = list(map(int, input().split()))
    females = list(map(int, input().split()))
    
    print(max_pairs(n, m, males, females))


if __name__ == "__main__":
    main()
