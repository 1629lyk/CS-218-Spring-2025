# A. Seating Arrangements

**Time limit per test:** 0.5 seconds  
**Memory limit per test:** 256 megabytes  

---

## Problem Description

There are **𝑛 families**. The 𝑖-th family has **𝑎𝑖** family members.  
All families will travel using a single bus consisting of **𝑟 rows**, with **2 seats** per row.

A person is considered **happy** if:
- Another family member is seated in the same row as them, **or**
- They are sitting **alone** in their row (with an empty seat next to them).

Your task is to determine the **maximum number of happy people** in an optimal seating arrangement.  
**Note:** Every person must be seated on the bus.

It is guaranteed that all family members will fit on the bus. Formally:

\[
\sum_{i=1}^{n} a_i \leq 2r
\]

---

## Input

Each test contains multiple test cases.  
- The first line contains a single integer **𝑡** (**1 ≤ 𝑡 ≤ 1000**) — the number of test cases.
- The description of the test cases follows.

Each test case contains:
- The first line with two integers **𝑛** and **𝑟** (**1 ≤ 𝑛 ≤ 100**, **1 ≤ 𝑟 ≤ 500**) — the number of families and the number of rows.
- The second line with **𝑛** integers **𝑎₁, a₂, ..., aₙ** (**1 ≤ 𝑎ᵢ ≤ 10**) — the number of family members in each family.

---

## Output

For each test case, output a single integer — the maximum number of **happy people** in an optimal seating arrangement.

---

## Example

### Input
```
4
3 3
2 3 1
3 3
2 2 2
4 5
1 1 2 2
4 5
3 1 1 3
```

### Output
```
4
6
6
6
```

---

## Explanation

### First Test Case
- Family 1: 2 members
- Family 2: 3 members
- Family 3: 1 member

Seating Plan:
```
Row 1: 1 1
Row 2: 2 2
Row 3: 2 3
```
- The two members of the first family sit together.
- Two members of the second family sit together.
- The last member of the second family sits with a member of the third family.

Here, **4 people** are happy (marked in green).

---

### Second Test Case
Seating Plan:
```
Row 1: 3 3
Row 2: 1 1
Row 3: 2 2
```
- Each row has two family members sitting together.
- **All 6 people are happy.**

---

### Third Test Case
Seating Plan:
```
Row 1: 4 4
Row 2: 2
Row 3: 3 3
Row 4: 1
```
- Members of the same families sit together or alone where necessary.
- **6 people** are happy.

---

## Notes

In each case, the arrangement is designed to maximize the number of happy people, following the defined conditions.

---