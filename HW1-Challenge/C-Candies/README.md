# C. Share Candies

### Problem Description

One day, 𝑛 CS141 students were talking about the candies they had earned. Some students became frustrated because they had fewer candies than others. Finally, they all agreed: some students would give their candies to others, so that everyone would end up with at least 𝑚 candies.

The 𝑛 students are located along the same street. The 𝑖-th student is at coordinate 𝑙𝑖 and initially has 𝑎𝑖 candies.  
However, during the transfer:
- A student **eats one candy per unit distance** they travel while giving candies to another student.
- Thus, if student 𝑖 tries to give 𝑥 candies to student 𝑗, then student 𝑗 only receives `x - |lᵢ - lⱼ|` candies.

### Task

Given the coordinates and the number of candies of all students, determine the **maximum possible number `m`** such that all students can eventually have at least `m` candies.

---

### Input

- The first line contains a single integer 𝑛 (1 ≤ 𝑛 ≤ 10⁵) — the number of students.
- The next 𝑛 lines each contain two integers 𝑙𝑖 and 𝑎𝑖 — the position and the initial candies of the 𝑖-th student.

**Note:**  
- For 30% of the test cases, 𝑛 ≤ 500.
- You should use 64-bit integers to avoid overflow.

---

### Output

- Output a single integer — the **maximum** number of candies 𝑚 that each student can finally have.

---

### Examples

#### Example 1
**Input:**
```
4
20 300
40 400
340 700
360 600
```

**Output:**
```
415
```

#### Example 2
**Input:**
```
10
13 5
26 54
39 7
49 59
61 56
73 26
85 13
97 38
110 52
120 31
```

**Output:**
```
26
```

#### Example 3
**Input:**
```
10
18 50
25 543
32 72
59 592
68 563
79 266
89 134
92 382
113 522
125 313
```

**Output:**
```
333
```

#### Example 4
**Input:**
```
10
2 20
4 21
6 22
8 23
10 24
12 25
14 26
16 27
18 28
20 29
```

**Output:**
```
22
```

#### Example 5
**Input:**
```
10
130 15
260 15
390 15
490 18
610 13
730 20
850 21
970 15
1100 17
1200 19
```

**Output:**
```
13
```

---

### Note on Example 1

There are 4 students, located at coordinates 20, 40, 340, and 360 on the street.  
After optimal transfers and accounting for distance-eaten candies:

- Student 1 initially has 300 candies.
- Student 2 sends candies to Student 1; after accounting for the 20 distance loss, Student 1 can reach 415 candies.
- Transfers continue similarly, accounting for distances and candy losses.
- Finally, **each student has exactly 415 candies**, which is the maximum achievable.

---
