# A. Water Refill

**Time Limit:** 1 second
**Memory Limit:** 256 megabytes

## Problem Description

Due to the increased interest in coming to school at UCR, the faculty decided to build a new dormitory named **South District**, home to a million students. To reduce waiting times in lines, the architects installed **100,000 faucets**! However, even with all these faucets, the students still experience long wait times, especially those at the back of the line. As a result, students now need to fill larger amounts of water, with some containers holding up to **100,000 units** of water.

There are **`m` faucets** in the water room. Each faucet:

* Can only serve **one student at a time**
* Dispenses **1 unit of water per second**

There are **`n` students**, each standing in a line and ready to fill their water containers.
Each student `i` needs `w[i]` units of water.

### Filling Rules:

* When the simulation begins, the **first `m` students** occupy the `m` faucets.
* Once a student finishes, the **next waiting student** immediately occupies the freed faucet.
* This transition is **instant** — if student `j` finishes at time `x`, the next student starts at time `x+1`.
* If there are fewer than `m` students left, only those faucets are used.

## Objective

Determine the **total time** required for **all students** to finish filling their water if they go in order.

---

## Input

* The first line contains two integers `n` and `m`

  * `(1 ≤ n ≤ 10^6)` — number of students
  * `(1 ≤ m ≤ 10^5 and m ≤ n)` — number of faucets

* The second line contains `n` integers:
  `w1 w2 ... wn` — the amount of water each student needs

  * `(1 ≤ wi ≤ 10^5)`

---

## Output

Print a single integer — the **total time** (in seconds) required for all students to fill their water.

---

## Examples

### Input

```
5 3
62 60 15 30 52
```

### Output

```
97
```

### Input

```
10 4
4 37 71 16 28 34 28 87 39 43
```

### Output

```
124
```

---

## Explanation

In the first example:

* Students 1, 2, 3 start first (using all 3 faucets).
* Student 3 only needs 15 units and finishes first.
* Student 4 starts at time 16 and needs 30 units → finishes at 45.
* Student 5 starts at time 46 and needs 52 units → finishes at 97.

The **last faucet to finish** is at time `97`, which is the total time needed.
