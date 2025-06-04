# D. Go Cycling

**Time limit per test:** 3 seconds  
**Memory limit per test:** 256 megabytes

---

## Problem Description

Yan is going to ride a bike in the park this weekend. However, he is too lazy and only wants to ride **downhill**. Specifically, the park can be represented as an **n-by-m grid**, and each cell of the grid has a corresponding height *h*.  

Yan can ride from a cell `(x, y)` to one of its four neighbors `(x', y')` **iff** `h[x][y] > h[x'][y']`.


There is an **entrance** in every cell of the **top row** and an **exit** in every cell of the **bottom row**.  

- Every entrance requires a **ticket** with a unit cost.  
- Once Yan buys a ticket for a particular entrance cell, he can **re-enter** it for **free** any number of times.  
- There is also a **free shuttle** between every exit and entrance. That means, **after reaching an exit**, Yan can go back to **any entrance** instantly for free.

Yan wants to visit **every exit** and is wondering:

- Is it possible to reach all exits?  
- If yes, what is the **minimum cost** (number of entrance tickets) required?

---

**Input**

- The first line contains two integers `n` and `m`  
  (`1 <= n, m <= 2 * 10^3`) — the number of rows and columns respectively.  
- The next `n` lines each contain `m` integers: the height values of the grid  
  (`0 <= h[i][j] <= 10^9`)


---

**Output**

- If Yan **can** reach **all exits**, print `1` on the first line, then print the **minimum number of tickets** required on the second line.
- Otherwise, print `0` on the first line, and print the **number of exits he can reach** on the second line.

---

## Examples

**Input**
```
5 5
10 9 8 9 10
7 7 5 5 5
4 4 4 4 4
3 3 3 3 3
2 1 2 1 2
```

**Output**
```
1
2
```

---

**Input**
```
2 5
9 1 5 4 3
8 7 6 1 2
```

**Output**
```
1
1
```

---

**Input**
```
3 6
8 4 5 6 4 4
7 3 4 3 3 3
3 2 2 1 1 2
```

**Output**
```
1
3
```

---

## Note

Try to use **efficient input functions** when implementing your solution to handle large input sizes.
