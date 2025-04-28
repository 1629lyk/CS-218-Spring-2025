import sys
input = sys.stdin.readline

"""
Sharing candies with distance at cost
Used Binary search with greedy algorithm to search for maximum candies for students to have atleast x candies
Ref:
1. Prof Yan Gu's slide - 05-greedy: Binary serach and Flower Vines
"""


def can_distribute_max(target_candies, positions, candies):
    n = len(candies)
    candies_surplus = 0  

    for i in range(n - 1):
        candies_surplus += candies[i] - target_candies
        distance = positions[i + 1] - positions[i]

        if candies_surplus >= 0: # positive surplus
            candies_surplus = max(0, candies_surplus - distance)
        else: # negative surplus -> corner cases like for ex. large distance lesser candies
            candies_surplus -= distance
        
    candies_surplus += candies[-1] - target_candies 
    return candies_surplus >= 0


def highest_candies_poss(students):
    # students.sort() # handling sorted data already
    positions = [pos for pos, _ in students]
    candies = [candy for _, candy in students]

    low = 0
    high = max(candies) or 10**19
    best_possible = 0

    while low <= high:
        mid = (low + high) // 2
        if can_distribute_max(mid, positions, candies):
            best_possible = mid
            low = mid + 1
        else:
            high = mid - 1

    return best_possible


def main():
    n = int(input())
    students = []
    for _ in range(n):
        position, candy_count = map(int, input().split())
        students.append((position, candy_count))

    print(highest_candies_poss(students))

if __name__ == "__main__":
    main()
