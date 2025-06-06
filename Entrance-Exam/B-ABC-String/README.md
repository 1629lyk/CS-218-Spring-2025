
# B. ABC String

**Time limit per test:** 0.5 seconds  
**Memory limit per test:** 256 megabytes  

## Problem Statement

For an integer `k`, define the ABC string at level `k` recursively as follows:

```
S₁ = "ABC"  
Sₖ = "A" + Sₖ₋₁ + "B" + Sₖ₋₁ + "C", for k ≥ 2
```

Here, `+` denotes string concatenation.

---

## Task

Given the level `k`, and two indices `l` and `r`, **extract the substring from the `l`-th to the `r`-th character of `Sₖ`**.

You must do this **efficiently** without explicitly building `Sₖ`, as its size grows exponentially.

---

## Input

- The first line contains an integer `t` (1 ≤ t ≤ 10⁴) — the number of test cases.
- Each of the following `t` lines contains three integers `k`, `l`, `r`:
  - 1 ≤ k ≤ 50  
  - 1 ≤ l ≤ r ≤ |Sₖ|  
  - 1 ≤ r − l + 1 ≤ 100

---

## Output

For each test case, output a single line: the substring from position `l` to `r` in `Sₖ`.

---

## Example

### Input
```
4
2 3 6
1 1 2
10 123 139
25 302727 302747
```

### Output
```
BCBA
AB
BAAABCBABCCBAABCB
CBABCCBAABCBABCCCCBAA
```

---

## Explanation

- **Test Case 1**:  
  S₂ = `A + "ABC" + B + "ABC" + C`  
     = `AABCBAABC`  
  Characters 3 to 6 are: **BCBA**

- **Test Case 2**:  
  S₁ = `"ABC"`  
  Characters 1 to 2 are: **AB**

---

## Constraints Recap

- You must **not build Sₖ explicitly**.
- Instead, recursively or iteratively **simulate traversal** using precomputed string lengths.
- Length of `Sₖ` is:  
  ```
  L₁ = 3  
  Lₖ = 2 * Lₖ₋₁ + 3
  ```

---

## Efficiency

- Precompute all `lengths[k]` up to 50.
- Use an iterative or recursive approach to find the character at position `pos` in `Sₖ`.
- Simulate traversal through:
  ```
  Sₖ = A + Sₖ₋₁ + B + Sₖ₋₁ + C
  ```
  to decide which segment contains the position.

---

## Resources

- [Recursion in Python](https://www.w3schools.com/python/gloss_python_function_recursion.asp)
---
