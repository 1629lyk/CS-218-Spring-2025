# C. The Met

**Time Limit:** 1 second  
**Memory Limit:** 256 megabytes

## Problem Description

Yihan was recently hired by the Metropolitan Museum of Art to help improve the visitor's experience. After some time, she realized that the current brochure provided at the entrance contains too little information, as the Met is very large.

Adding everything into one brochure would make it too heavy and wasteful since a visitor typically visits only specific regions (like the Medieval Art, Arms and Armor, or the Islamic Wing) in a single day.

To solve this, Yihan decides to place brochure booths inside each region that provide in-depth information **only when the visitor enters that area**.

However, each collection region is still quite big. Each region contains a total of `n` exhibits (think of them as paintings or rooms), and the layout is in the form of a **tree** (i.e., there is only one way to travel from one exhibit to another). Visitors spend exactly one unit of time per exhibit (walking time is negligible).

The goal is to **place the brochure booth in one exhibit** such that the **maximum time** it takes to reach any other exhibit from there is **minimized**.



## Input

- The first line contains an integer `n` (1 ≤ n ≤ 100,000) — the number of exhibits.
- Each of the following `n − 1` lines contains two integers `i` and `j` (1 ≤ i, j ≤ n), indicating that exhibit `i` and exhibit `j` are connected by a path.



## Output

- Output a single integer: the **maximum distance** from the brochure booth to the farthest exhibit when placed optimally.



## Example Input 1

```
4
1 2
2 3
2 4
```

### Example Output 1
```
1
```



## Example Input 2

```
8
1 2
2 3
3 4
2 5
5 6
6 7
5 8
```

### Example Output 2
```
3
```



## Explanation

In the second example, the region can be visualized as shown below:

![Tree Diagram](https://espresso.codeforces.com/f4011dd7b118a1dd39459567c795f7dce29a4f25.png)

The best exhibit to place the brochure booth is at node `2` or `5`. In either case, the **maximum distance to the farthest exhibit** is `3`.



## Constraints

- `1 ≤ n ≤ 10⁵`
- The graph is guaranteed to be a tree.