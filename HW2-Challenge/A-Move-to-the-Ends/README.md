# A. Move to the Ends

## Problem Statement

You are given an array of `n` integers, containing a **permutation** of the integers `1, 2, ..., n`.  
You can perform the following two operations in any order:

- **Move an element to the beginning** of the array.
- **Move an element to the end** of the array.

Your goal is to **sort the array in ascending order** with the **minimum number of operations**.

---

## Input Format

- The first line contains an integer `t` — the number of test cases `(1 ≤ t ≤ 10⁴)`.
- Each test case consists of:
  - A single integer `n` `(1 ≤ n ≤ 2 × 10⁵)` — the size of the array.
  - A line with `n` integers `a₁, a₂, ..., aₙ` — the permutation of integers from `1` to `n`.

**Constraints:**
- The sum of `n` over all test cases does not exceed `2 × 10⁵`.

---

## Output Format

For each test case, output a single integer — the minimum number of operations needed to sort the array.

---

## Example

### Input
```
3
6
2 3 1 6 4 5
3
3 2 1
4
1 2 3 4
```

### Output
```
2
2
0
```

---

## Explanation

- **First Test Case:**
  - Initial array: `[2, 3, 1, 6, 4, 5]`
  - Move `1` to the beginning → `[1, 2, 3, 6, 4, 5]`
  - Move `6` to the end → `[1, 2, 3, 4, 5, 6]`
  - Total operations: **2**

- **Second Test Case:**
  - Initial array: `[3, 2, 1]`
  - Move `1` to the beginning → `[1, 3, 2]`
  - Move `2` to the end → `[1, 3, 2]` → `[1, 2, 3]` (after rearrangement)
  - Total operations: **2**

- **Third Test Case:**
  - Initial array: `[1, 2, 3, 4]`
  - Already sorted, no operations needed.
  - Total operations: **0**
