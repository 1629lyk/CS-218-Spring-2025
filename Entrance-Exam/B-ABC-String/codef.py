MAX_K = 50 # upper most bound found in problem
lengths = [0] * (MAX_K + 1)

def precomp_len():
    lengths[1] = 3 
    for k in range(2, MAX_K + 1):
        lengths[k] = 2 * lengths[k - 1] + 3 # "ABC"

# forms char without generating full string 
def char_in_range(k, pos):
    while k > 1: 
        
        len_k1 = lengths[k - 1] # reach to S_1
        
        if pos == 1:
            return 'A' 
        
        elif pos == 1 + len_k1 + 1: # middle side of S_k-1 
            return 'B'

        elif pos <= 1 + len_k1: # near first side of S_k-1
            pos -= 1 # skip A
            k -= 1 # move to previous stakc layer
        
        elif pos <= 1 + len_k1 + 1 + len_k1:
            pos -= (1 + len_k1 + 1) # the same but for middle segment 
            k -= 1
        
        elif pos == lengths[k]:
            return 'C'
        
        else:
            return "" 
    
    first = "ABC"
    
    if 1 <= pos <= 3:
        return first[pos - 1] 
    
    else:
        return ""

def extract_chars(k, l, r):
    result = []
    for i in range(l, r + 1):
        if i > lengths[k]:
            result.append("") 
        else:
            result.append(char_in_range(k, i))
    return ''.join(result)


def main():
    precomp_len()
    t = int(input())
    for _ in range(t):
        k, l, r = map(int, input().split())
        print(extract_chars(k, l, r))


if __name__ == "__main__":
    main()
