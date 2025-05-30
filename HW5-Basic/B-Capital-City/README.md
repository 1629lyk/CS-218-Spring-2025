# B. Capital City

## Problem Statement

Yihan is building a kingdom in a game. She has built `n` cities connected with `m` **unidirectional** roads. The cities are numbered from 1 to `n`.

She now wants to choose a **capital city**. For security reasons, the capital must be **reachable from all other cities** (i.e., there must be a path from every city to the capital).

Your task is to compute:
- The number of such candidate cities.
- List all of them in **increasing order**.

---

## Input

- The first line contains two integers `n` and `m`  
  (1 ≤ `n` ≤ 100,000, 1 ≤ `m` ≤ 200,000)

- The next `m` lines each contain two integers `a` and `b`  
  (1 ≤ `a`, `b` ≤ `n`), indicating a one-way road from city `a` to city `b`.

---

## Output

- Print one integer: the number of candidate cities.
- In the next line, print all the candidate cities in **increasing order** (space-separated).

---

## Example

### Input
```
4 4
1 2
3 2
4 3
2 1
```

### Output
```
2
1 2
```

---

## Constraints
- Use efficient algorithms such as **Kosaraju’s or Tarjan’s algorithm** for SCC detection.
- Time and memory limits are strict for large graphs.
- String or array sizes should be optimized to stay within bounds (max substring length up to 10^3 for individual nodes in explanations or logs).

---

## Hint

After finding strongly connected components (SCCs), find the **sink SCC** (no outgoing edges in the condensed graph). If it's **unique**, every node in that component is a valid capital.
