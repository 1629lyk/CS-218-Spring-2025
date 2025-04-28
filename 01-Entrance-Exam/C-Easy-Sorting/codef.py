def easy_swap(n, candies):
    swapss = 0
    
    count = [0, 0, 0, 0] # extra index making me easy to handle indexes
    for candy in candies:
        count[candy] += 1

    misplaced = [[0]*4 for _ in range(4)]

    
    for i in range(0, count[1]):
        misplaced[1][candies[i]] += 1
    
    for i in range(count[1], count[1] + count[2]):
        misplaced[2][candies[i]] += 1
    
    for i in range(count[1] + count[2], n):
        misplaced[3][candies[i]] += 1

    
    for i in range(1, 4):
        for j in range(i + 1, 4):
            d = min(misplaced[i][j], misplaced[j][i]) 
            swapss += d
            
            
            misplaced[i][j] -= d
            misplaced[j][i] -= d

    
    # this will fix all misplacements, breaks the swap cycle
    rem_add_up = (
        misplaced[1][2] + misplaced[1][3] +
        misplaced[2][1] + misplaced[2][3] +
        misplaced[3][1] + misplaced[3][2]
    )
    swapss += 2 * (rem_add_up // 3) 

    return swapss


def main():
    n = int(input())
    candies = []
    for _ in range(n):
        val = int(input())
        candies.append(val)

    result = easy_swap(n, candies)
    print(result)

if __name__ == "__main__":
    main()
