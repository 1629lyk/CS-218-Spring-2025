# B. Secret Message

## Problem Description

As an adventurer, you have wandered the world in search of a legendary treasure chest and have finally arrived at a remote area where the treasure is said to lie. According to legend, alphabet letters are scattered all over this area, and it is said that you can decipher the secret message to find the treasure chest using these letters as clues.

The area is represented as a two-dimensional grid with **N** rows and **M** columns, and each cell contains one lowercase alphabet letter. 

Your goal:
- Start from the top-left square (1,1).
- Trace only adjacent squares (up, down, left, or right) **in order** to the bottom-right square (N,M).
- You **cannot pass through any square more than once**.
- You **cannot leave the grid boundaries**.
- Among all valid paths, the secret message is the **smallest alphabetical message** you can form.

Can you decipher the secret message and unlock the treasure chest?

---

## Input Format
- The first line contains two integers `N` and `M` — the number of rows and columns respectively.
- The next `N` lines each contain a string of `M` lowercase letters representing the grid.

**Constraints:**
- \( 1 \leq N \leq 6 \)
- \( 1 \leq M \leq 5 \)
- Each character is a lowercase English letter ('a' to 'z').

---

## Output Format
- Output a single line containing the **smallest lexicographical message** obtained by traversing the grid according to the rules.

---

## Examples

### Example 1
**Input:**
```
3 5
hello
ganyu
world
```
**Output:**
```
heagworld
```

### Example 2
**Input:**
```
5 5
youzz
zzgot
zzzza
erces
tzzzz
```
**Output:**
```
yougotasecretzzzz
```

### Example 3
**Input:**
```
3 3
abc
bcx
cyz
```
**Output:**
```
abcbcxz
```

---

## Notes
- You must move carefully across adjacent squares without revisiting any cell.
- The goal is to construct the **lexicographically smallest string** among all possible valid paths.
- Depth-first search (DFS) with pruning based on the current prefix compared to the best-so-far string is an efficient approach for this problem.

---