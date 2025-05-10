"""
Understanding the Problem:
We are given a set of courses, each with a credit value and possibly a prerequisite course. 
If a course has a prerequisite, it must be taken simultaneously. 
Our goal is to select at most 'm' courses to maximize total credit, 
while respecting prerequisite dependencies. 
This problem forms a forest of dependency trees. 
Each tree's selection must be "ancestor-closed" — if we select a course, 
we must also select its prerequisite chain.

Plan of Attack:
- Represent the prerequisite structure as a forest of trees using an adjacency list.
- Use a recursive DFS with dynamic programming to compute optimal credit selection within each subtree:
    - dp_u[k] stores the maximum credit achievable by selecting exactly k nodes in the subtree rooted at u.
    - Initialize with dp_u = [0, credit[u]] to handle base case of picking no nodes or just the root.
    - For each child v, merge dp_v into dp_u using a knapsack-style convolution, avoiding selection of descendants without their parent.
- Once all trees are processed, combine their results via a top-level knapsack DP:
    - dp_all[i] stores the best credit possible with exactly i total courses across all trees.
    - Merge each tree's dp table into the global dp_all while respecting the course count limit m.

Time Complexity:
- Each course is visited once in the DFS, and each DP table merge takes up to O(m^2) time.
- Total time complexity is within O(n * m^2), for n ≤ 300 and m ≤ 300.

References:
1. https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
2. https://codeforces.com/blog/entry/20935
3. https://www.geeksforgeeks.org/dp-on-trees-for-competitive-programming/

"""

from functools import lru_cache
NEG_INF = -10**15

@lru_cache(None)
def dfs(u):
    # dp_u[k] = best credit picking exactly k nodes in u's subtree
    dp_u = list()
    dp_u = [0, credit[u]]    # dp_u[0]=0, dp_u[1]=credit[u]
    u_size = 1

    for v in chd[u]:
        dp_v, v_size = dfs(v)
        n_size = min(u_size + v_size, m)
        n_dp = [NEG_INF] * (n_size + 1)

        for i in range(u_size+1):
            if dp_u[i] == NEG_INF:
                continue
            
            
            for j in range(v_size+1):
                if dp_v[j] == NEG_INF:
                    continue
                # can't pick descendants if we haven't picked u
                
                
                if i == 0 and j > 0:
                    continue
                if i + j > n_size:
                    continue
                
                val = dp_u[i] + dp_v[j]
                
                if val > n_dp[i+j]:
                    n_dp[i+j] = val

        dp_u, u_size = n_dp, n_size

    return tuple(dp_u), u_size


n, m = map(int, input().split())
chd = [[] for _ in range(n+1)]
credit = [0]*(n+1)
roots = []


for i in range(1, n+1):
    p, c = map(int, input().split())
    credit[i] = c
    
    
    if p == 0:
        roots.append(i)
    else:
        chd[p].append(i)


# global knapsack over the separate trees
dp_all = [NEG_INF] * (m+1)
dp_all[0] = 0

for r in roots:
    dp_r, _ = dfs(r)
    n_dp = [NEG_INF] * (m+1)
    
    for i in range(m+1):
        if dp_all[i] == NEG_INF:
            continue
        
        for j, rv in enumerate(dp_r):
            if rv == NEG_INF or i + j > m:
                continue
            
            cand = dp_all[i] + rv
            if cand > n_dp[i+j]:
                n_dp[i+j] = cand
    
    
    dp_all = n_dp

print(dp_all[m])
