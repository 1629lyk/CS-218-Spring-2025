"""
Understanding the Problem:

So we are given a string of candies, where each character represents a flavor.
Each flavor (limited to first k lowercase letters) has an associated cost.
The goal is to make the given string symmetric that is a palindrome by only inserting characters
at any position, and each insertion has a cost based on the flavor.

The aim is to find the minimum total cost required to convert the string into a palindrome.

Constraints:
- Only insertions are allowed; deletions or replacements are not permitted.
- We must preserve the original characters since the string was given for free.
- We can insert any number of candies, using flavors from the first k letters.

Plan of Attack:
- Use dynamic programming to calculate the minimum insertion cost.
- Let dp[i][j] represent the minimum cost to make the substring s[i..j] a palindrome.
- If the characters at both ends (s[i] and s[j]) are equal, no insertion is needed at this level
  we take the result from the inner substring dp[i+1][j-1].
- Otherwise, we consider two options:
  (1) Insert s[i] after position j — cost becomes dp[i+1][j] + cost of s[i]
  (2) Insert s[j] before position i — cost becomes dp[i][j-1] + cost of s[j]
  Take the minimum of the two to update dp[i][j].

- Fill the dp table diagonally by increasing substring lengths (bottom-up approach).
- The final answer will be in dp[0][n-1], which gives the minimum cost to make the full string symmetric.

Time Complexity:
- We process all substrings of length up to n.
- For each substring (i, j), we perform O(1) work.
- Total complexity: O(n^2), where n is the length of the string.

Space Complexity:
- O(n^2) space for the DP table.

Example:
For s = "abb" and costs a=5, b=1:
- Inserting two 'b's at the beginning yields the palindrome "bbabb", costing 2.
- This is cheaper than inserting 'a' at the end to make "abba", which costs 5.

References:
1. https://www.youtube.com/watch?v=EN7yGmZ9v2M
2. https://www.geeksforgeeks.org/minimum-insertions-to-form-a-palindrome-dp-28/
3. https://stackoverflow.com/questions/57178027/find-minimum-cost-to-convert-to-palindrome
"""


n, k = input().split()
k = int(k)


w = {}
for i in range(k):
    cost = int(input())
    w[chr(ord('a') + i)] = cost


s = input().strip()
n = len(s)


dp = [[0]*n for _ in range(n)] # dp table

c1, c2 = int(0), int(0)

for l in range(2, n+1):
    
    for i in range(n - l + 1):
        j = i + l - 1
    
        if s[i] == s[j]:
            dp[i][j] = dp[i+1][j-1]
    
    
        else:
            # either s[i] -> right end, or s[j] -> left end
            c1 = dp[i+1][j] + w[s[i]]
            c2 = dp[i][j-1] + w[s[j]]
            
            if c1 < c2:
                dp[i][j] = c1
            else:
                dp[i][j] = c2


print(dp[0][n-1])
