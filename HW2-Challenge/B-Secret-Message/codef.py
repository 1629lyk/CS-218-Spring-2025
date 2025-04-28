"""
The plan of attack is to find the lexicographically smallest path from the top-left (1,1) to the bottom-right (N,M) in a given grid, 
moving only to adjacent cells (up, down, left, right) without revisiting any cell.

The steps would be:
1. Start DFS traversal from the (0,0) cell with the initial prefix string.
2. Then at each step, collect all unvisited neighbors and sort them lexicographically based on the letter.
3. Prune paths early if the current prefix cannot possibly lead to a better solution than the best so far.
4. Upon reaching (n-1, m-1), compare the current path string and update the best result if necessary.

This makes sure that paths are explored in such a way which prioritizes forming the smallest possible string at each decision point.

Time Complexity:
1. Exploring paths using DFS - worst case exponential in number of cells O(4^(N x M)), 
   but aggressive pruning reduces actual exploration significantly.
2. Sorting neighbors at each step: O(1) in practice due to at most 4 neighbors (fixed).

Hence, Upper Bound is O(4^(N x M))

Thus, for the given constraints (N ≤ 6, M ≤ 5), the solution runs efficiently within the limits.

References:
1. https://stackoverflow.com/questions/29376069/lexographically-smallest-path-in-a-nm-grid
2. https://www.geeksforgeeks.org/print-the-lexicographically-smallest-dfs-of-the-graph-starting-from-1/

Side Note:
Initially tried solving with a heap (priority queue) approach to always expand the path with the smallest string first.
It did fail on some test cases, I guess it is because the heap makes greedy global decisions without considering better local paths.

Come back to this later:
The correct approach here is to use DFS with local neighbor sorting at each step, 
which ensures that we always explore the best lexicographic options locally before committing,
guaranteeing the overall smallest message.
"""


N, M = map(int, input().split())
grid = [input().strip() for _ in range(N)]

def smallest_message(grid):
    
    n = len(grid)
    m = len(grid[0])
    best = ['{' * (n * m + 1)]  # It is Lexicographically greater than any valid string

    dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # RDUL -> direction

    vis = [[False] * m for _ in range(n)]
    vis[0][0] = True
    

    dfs(0, 0, grid[0][0], grid, n, m, vis, best, dir)
    return best[0]

def dfs(x, y, prefix, grid, n, m, vis, best, dir):
    
    if len(prefix) >= len(best[0]) and prefix == best[0][:len(prefix)]:
        return
    
    # Remove it if current path is not found to be better than the other choice so far
    if prefix > best[0][:len(prefix)]:
        return
    

    if x == n - 1 and y == m - 1:
        if prefix < best[0]:
            best[0] = prefix
        return

    neig = []
    for dx, dy in dir:
        
        nx, ny = x + dx, y + dy
        
        
        if 0 <= nx < n and 0 <= ny < m and not vis[nx][ny]:
            neig.append((grid[nx][ny], nx, ny))
    
    neig.sort()  # It is Lexicographically smallest options first

    for ch, nx, ny in neig:
        vis[nx][ny] = True
        dfs(nx, ny, prefix + ch, grid, n, m, vis, best, dir)
        vis[nx][ny] = False

print(smallest_message(grid))
