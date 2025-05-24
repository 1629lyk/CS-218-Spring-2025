"""
Understanding the Problem:

We are given a string of digits, and the task is to 
split it into the maximum number of contiguous substrings 
such that the sequence of substrings forms a palindrome. 
That means if the substrings are [s1, s2, ..., sk], 
then s1 == sk, s2 == s(k-1), and so on.

Example:
For string "179791", we can split it as ["1", "79", "79", "1"] 
which forms a palindrome and has 4 parts.

this solution uses a rolling hash approach 
to compare substrings efficiently in O(1) time,

as Naive substring comparisons (like s[i:j] == s[k:l]) 
are slow for large inputs (up to 10^6 digits)

Plan of Attack:
- For each test case, compute forward rolling hashes 
       for the string under two large moduli.
- Use two pointers `i` and `j` starting from both ends of the string.
- Try to find the smallest matching prefix and 
       suffix (s[i:i+d] == s[j-d+1:j+1]) using precomputed hashes.
- If a match is found, remove those parts and count +2 parts.
- If no match is found, the remaining 
       middle is one unmatched chunk, counted as +1.
- If one character is left after all matches, count it as +1.

Why Double Hashing:
- Hash collisions can cause incorrect matches.
- Using two different moduli makes it impossible to have false positives.

Hashing Details:
- BASE is a large constant used in polynomial hashing.
- We precompute BASE^k modulo MOD1 and MOD2 
       to allow fast O(1) substring hash computation.
- We compute prefix hashes for the entire string, 
       then use them to compute any substring hash in constant time.

Time Complexity:
- Each test case runs in O(n) due to rolling hash and early break after a successful match.
- Total complexity is O(sum(s)) across all test cases, where s -> 10^6.

This approach ensures correctness and efficiency even for large inputs.

References:
1. https://codeforces.com/blog/entry/60445 
2. https://cp-algorithms.com/string/string-hashing.html 
3. https://stackoverflow.com/questions/4008541/how-to-split-a-string-into-as-few-palindromes-as-possible
4. 
"""


import sys
input = sys.stdin.readline
 
t = int(input())
inp_s = [input().strip() for _ in range(t)]
max_n = max(len(s) for s in inp_s)
 
 
BASE = 9999999
MOD1 = 10**9 + 7
MOD2 = 10**9 + 9
 
# Precompute BASE^k mod each prime
pow1 = [1] * (max_n + 1)
pow2 = [1] * (max_n + 1)
for i in range(1, max_n + 1):
    pow1[i] = pow1[i-1] * BASE % MOD1
    pow2[i] = pow2[i-1] * BASE % MOD2
 
def max_parts(s):
    n = len(s)
 
    h1 = [0] * (n+1)
    h2 = [0] * (n+1)
    for idx, ch in enumerate(s):
        o = ord(ch)
        h1[idx+1] = (h1[idx] * BASE + o) % MOD1
        h2[idx+1] = (h2[idx] * BASE + o) % MOD2
 
    parts = 0
    i = 0 
    j = n-1
    
    
    while i < j:
    
    
        found = False
        half = (j - i + 1) // 2
        for d in range(1, half+1):
 
    
            pre1 = (h1[i+d] - h1[i] * pow1[d]) % MOD1
            pre2 = (h2[i+d] - h2[i] * pow2[d]) % MOD2
 
 
    
            l = j - d + 1
            suf1 = (h1[j+1] - h1[l] * pow1[d]) % MOD1
            suf2 = (h2[j+1] - h2[l] * pow2[d]) % MOD2
 
            if pre1 == suf1 and pre2 == suf2:
                parts += 2
                i += d
                j -= d
                found = True
                break
 
        if not found:
            # take the remainder as one part
            parts += 1
            return parts
 
    # if exactly one character left in the center
    if i == j:
        parts += 1
    return parts
 
 
out = []
for s in inp_s:
    out.append(str(max_parts(s)))
sys.stdout.write("\n".join(out))
