"""
Algorithm Explanation:

So for a given 2D grid for a ski resort, each cell stores the value of the elevation. 
Now the goal is to determine the length of longest possible skiing path, 
moving only to adjacent cells in this direction -> up, down, left, right 
making sure there is a decreasing elevation values.

For efficiency a directed acyclic graph (DAG), is used
where each cell is a node, and edges point from higher to lower elevation neighbors. 
allowing for dynamic programming techniques as this structure ensures no repeated cycles.

Then perform a Depth-First Search (DFS) starting from each cell to explore all decreasing paths. 
Memoization is used to reeduce redundant computations and improving efficiency, that does the following:
we store the length of the longest path starting from each cell in a cache,
If a cell's longest path has already been computed, we use it from the cache instead of recalculating it.

By iterating through all cells and computing the longest decreasing path from each, 
we can determine the maximum path length across the entire grid.

Time Complexity:
1. Each cell is visited once, and during the DFS, we explore up to four directions (up, down, left, right).
2. Memoization ensures that each cell's longest path is computed only once.

Overall Time Complexity: O(r * c), where r is the number of rows and c is the number of columns.

References:
1. https://www.geeksforgeeks.org/longest-increasing-path-matrix/
2. https://www.youtube.com/watch?v=wCc_nd-GiEc
"""


r, c = map(int, input().split())
h = [list(map(int, input().split())) for _ in range(r)]

dp_table = [[0] * c for _ in range(r)]  

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

def dfs_explore(x, y):
    
    if dp_table[x][y] != 0:
        return dp_table[x][y]
    
    best = 1  

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c and h[nx][ny] < h[x][y]:
            best = max(best, 1 + dfs_explore(nx, ny))
    
    dp_table[x][y] = best
    return best

long = 0
for x in range(r):
    for y in range(c):
        long = max(long, dfs_explore(x, y))

print(long)
