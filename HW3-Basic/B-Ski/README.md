# Problem B: Ski

**Time Limit:** 2 seconds  
**Memory Limit:** 256 megabytes  

Skiing is fun! Basically speaking, you always ski from a higher location to a lower one.  
One day, Yihan went to a ski resort. The resort can be viewed as a rectangle (i.e., a 2D array) with `r` rows and `c` columns. The height at row `i` and column `j` in the resort is given by `h[i][j]`.

Your task is to help Yihan find the longest possible skiing path in the resort.



## Movement Rules

You can ski from a location `x` to a location `y` **if and only if**:

- `x` and `y` are adjacent. Each cell `(i, j)` has up to 4 neighbors:  
  - Up: `(i - 1, j)`  
  - Down: `(i + 1, j)`  
  - Left: `(i, j - 1)`  
  - Right: `(i, j + 1)`
- The height at `x` is **strictly greater** than the height at `y`.



## Example Grid

|  1  |  2  |  3  |  4  |  5  |
|--|--|--|--|--|
| 16  | 17  | 18  | 19  |  6  |
| 15  | 24  | 25  | 20  |  7  |
| 14  | 23  | 22  | 21  |  8  |
| 13  | 12  | 11  | 10  |  9  |


- A valid skiing path: `24 → 17 → 16 → 1` (length: 4)  
- The longest skiing path: `25 → 24 → 23 → ... → 3 → 2 → 1` (length: **25**)



## Input Format

- The first line contains two integers `r` and `c`  
  `(1 ≤ r, c ≤ 1000)`

- The next `r` lines each contain `c` integers:  
  The height values for the ski resort grid.  
  The `j`-th integer in the `i`-th row is `h[i][j]`.  

- All `h[i][j]` values are in the range `[0, 10⁹]`.

You can score **60%** of the points if your algorithm works for `r, c ≤ 100`.



## Output Format

Output a single integer — the **length of the longest skiing path**.



## Sample Input 1
```
5 5
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
```
### Sample Output 1

25



## Sample Input 2
```
5 5
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
```
### Sample Output 2
9

## Notes

- You can start skiing from **any cell** in the grid.
- You are only allowed to move to a strictly **lower** adjacent cell.
- Use **Dynamic Programming with Memoization** or **DFS with Caching** for optimal performance.
- Avoid recalculating the longest path from a cell if it's already computed.



