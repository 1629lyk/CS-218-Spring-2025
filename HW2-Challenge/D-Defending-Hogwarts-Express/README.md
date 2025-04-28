# D. Defending Hogwarts Express

## Problem Statement

During the First Wizarding War, Death Eaters attacked the Hogwarts Express, which was carrying students to Hogwarts. The railway can be viewed as a one-dimensional number line. Each train car \(i\) is at a position \(x_i\) and has a defense value \(D_i\) thanks to the enchantment *Protego totalum*.

Each Death Eater's attack has:
- **Attack value** \(A_j\)
- **Center position** \(y_j\)
- **Radius** \(b_j\)

The attack affects the railway in the range \([y_j - b_j, y_j + b_j]\), and destroys **any train car** in that range if its defense value is less than or equal to \(A_j\).

Each train car can only be destroyed once (earlier attacks take precedence).

Your task is to determine how many train cars are destroyed by each attack.

---

## Input

- The first line contains an integer \(n\) — the number of train cars.
- Each of the next \(n\) lines contains two integers:
  - \(x_i\) — the position of the \(i\)-th train car.
  - \(D_i\) — the defense value of the \(i\)-th train car.
- The next line contains an integer \(m\) — the number of attacks.
- Each of the next \(m\) lines contains three integers:
  - \(A_j\) — attack value
  - \(b_j\) — attack radius
  - \(y_j\) — center of attack

---

## Output

- Print \(m\) lines.
- Line \(i\) should contain a single integer — the number of train cars destroyed by the \(i\)-th attack.

---

## Example

### Input
```
4
1 1
2 3
5 2
10 8
3
2 3 3
6 4 8
10 4 5
```

### Output
```
2
0
1
```

---

## Explanation

- **First Attack (2 3 3)**:  
  Range = [0, 6].  
  Hits train cars at positions 1, 2, 5.  
  Destroys cars with defense ≤ 2 → cars at 1 (defense 1) and 5 (defense 2).

- **Second Attack (6 4 8)**:  
  Range = [4, 12].  
  Hits cars at 5, 10.  
  Car at 5 is already destroyed.  
  Car at 10 has defense 8, which is greater than attack value 6 → No destruction.

- **Third Attack (10 4 5)**:  
  Range = [1, 9].  
  Hits car at 2.  
  Car at 2 has defense 3, which is less than attack value 10 → Destroyed.

---

## Constraints

- \(1 \leq n, m \leq 100,000\)
- \(0 \leq D_i, A_j, x_i, y_j, b_j \leq 10^9\)

---

## Notes

- After a train car is destroyed, it cannot be destroyed again by future attacks.
- Efficient algorithms are necessary due to the high constraints on \(n\) and \(m\).
- A segment tree can be used to find and destroy train cars efficiently.

---

## References

- [Segment Trees - CP-Algorithms](https://cp-algorithms.com/data_structures/segment_tree.html)
- [Segment Tree Range Minimum Query - GeeksforGeeks](https://www.geeksforgeeks.org/segment-tree-range-minimum-query/)
- [Segment Trees Tutorial (YouTube)](https://www.youtube.com/watch?v=ciHThtTVNto)

---

> This problem appeared in UCRPC 2022.  
> Inspired by **Harry Potter and the Philosopher’s Stone** — J.K. Rowling.

---
