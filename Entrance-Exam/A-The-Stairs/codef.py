"""
Task to find Sheldon Step, find the faulty step
references:
https://stackoverflow.com/questions/13276235/verifying-arithmetic-sequence-python
"""

def sheldon_step(n, altt):
    diffs = [altt[i+1] - altt[i] for i in range(n - 1)] # should calculate diff in the series

    # Used Dictionary to store differences count like how frequent it is and have like unique key-value pairs
    freq = {}
    for d in diffs:
        freq[d] = freq.get(d, 0) + 1 

    # will store the frequent diff in the series 
    max_count = 0
    common_diff = None
    for diff, count in freq.items():
        if count > max_count:
            max_count = count
            common_diff = diff

    # logic that covers all corner cases like adjacent step disparaties and more in the sequences 
    for i in range(n - 1):
        if diffs[i] != common_diff:
            
            # check 1: next diff is valid then current step is bad (sheldon step)
            if i + 2 < n and altt[i+2] - altt[i+1] == common_diff:
                return i + 1  # 1-based index of altt[i]

            # check 2: skipping one gives valid jump then next step is bad
            elif i + 2 < n and altt[i+2] - altt[i] == 2 * common_diff:
                return i + 2  # 1-based index of altt[i+1]
            
            else:
                return i + 2 # assumed as shelfon step and considered as the fallback
            
    return -1 

def main():
    n = int(input())
    altt = [int(input()) for _ in range(n)]

    print(sheldon_step(n, altt))

if __name__ == "__main__":
    main()