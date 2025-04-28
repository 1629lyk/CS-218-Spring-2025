# C. Marathon

**Time limit per test:** 0.5 seconds  
**Memory limit per test:** 256 megabytes

This problem is from **UCRPC**, themed around the **2024 Summer Olympic Games**.

---

## Problem Statement

The marathon is a long-distance foot race with a distance of **42.195 km**.  
In this Marathon game, we aim to ensure that **every meter** of the race is covered by **at least two cameras** for broadcast quality.

However, camera placements are restricted to **pre-determined locations** along the course.  
The \( i \)-th possible camera is located at a distance \( x_i \) meters from the start, with a **coverage radius** of \( k_i \) meters — meaning it covers all points within \( k_i \) meters away from it.

For simplicity, the course is considered a **straight line** of exactly **42,195 meters**.

Your task is to **set up the minimum number of cameras** such that **every meter** of the race course is covered **at least twice**.  
If it is **impossible**, output `-1`.

---

## Input

- The first line contains an integer \( n \) — the number of possible camera locations.
- The next \( n \) lines each contain two integers \( x_i \) and \( k_i \):
  - \( x_i \): position of the camera from the start.
  - \( k_i \): the coverage radius of the camera.

**Note:**  
The total course length is always **42195 meters**.

---

## Output

- Output a single integer: the **minimum number of cameras needed** to guarantee that every position is **covered twice**.
- If it is **impossible**, output `-1`.

---

## Example

### Input
```
5
15000 20000
5000 10000
35000 10000
10000 5000
25000 20000
```

### Output
```
4
```

---

## Constraints

- For **50%** of the test data: \( n \leq 1000 \)
- For **100%** of the test data: \( n \leq 100000 \)

---

## Fun Facts About the Marathon 🏃‍♂️

The name **"Marathon"** comes from the legend of **Pheidippides**, the Greek messenger.

According to legend:
- After the Greeks defeated the Persian army at the **Battle of Marathon**,  
- Pheidippides ran from the Marathon plain to Athens to deliver the victory message.
- It is said he ran the entire distance **without stopping**, discarded his weapons and clothes to lighten his weight, and upon reaching Athens, cried "We have won!" before collapsing and dying.

The modern **Marathon-Athens highway** roughly follows one possible route of this legendary run, covering about **40 km**.  
Alternative historical routes suggest slightly different paths, one involving a steep climb but a slightly shorter distance of about **35 km (22 miles)**.

---

#  Source:
- Wikipedia: [Marathon (Legend)](https://en.wikipedia.org/wiki/Marathon)
