
# C. Easy Sorting

Yihan has a list of candies arranged in a sequence. Each candy has a **tastiness level** represented by an integer `tᵢ`, and there are only **three possible levels**: `1`, `2`, and `3`.

Yihan wants to sort the candies in **non-decreasing order of tastiness**, using the only operation she allows herself — an **"easy swap"**, where she can swap **any two elements** in the list (they don't have to be adjacent).

Your task is to determine the **minimum number of easy swaps** required to sort the list.

---

## Problem Statement

### Input

- The first line contains a single integer `n` — the number of candies.  
- The next `n` lines each contain an integer (`1`, `2`, or `3`), representing the tastiness level of each candy in order.

### Output

- A single integer representing the **minimum number of easy swaps** required to sort the list.

---

## Example

### Input
```
5  
2  
1  
3  
1  
2  
```

### Output
```
2
```

### Explanation
- Swap the first `2` and the second `1`:  
  → `[1, 2, 3, 1, 2]`
- Swap the third `3` and the fourth `1`:  
  → `[1, 2, 1, 3, 2]` → `[1, 1, 2, 3, 2]`
- Swap the fifth `2` and the fourth `3`:  
  → `[1, 1, 2, 2, 3]`  
Total swaps = **2**

---

## Constraints

- For 50% of the test cases: `1 ≤ n ≤ 100`
- For 100% of the test cases: `1 ≤ n ≤ 10⁵`
- All values are guaranteed to be either `1`, `2`, or `3`.

---

## Approach Summary

This problem can be solved efficiently by:

1. **Counting** the number of each type of candy (`1`, `2`, `3`).
2. **Dividing** the array into 3 segments representing where `1`s, `2`s, and `3`s should be in a sorted list.
3. **Building a misplacement matrix** to track which values are in the wrong segments.
4. **Fixing misplacements using direct swaps** between pairs of mismatched segments.
5. **Resolving leftover 3-way cycles** with 2 swaps per cycle.

This approach runs in **O(n)** time and uses **O(1)** extra space (besides the input array).

---

## 📎 Tags

- Greedy
- Sorting
- Arrays
- Swapping Strategy
- Optimization

---
