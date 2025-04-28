# B. Artistic Swimming

**Time Limit:** 2 seconds  
**Memory Limit:** 256 MB  

This problem is from UCRPC, themed around the 2024 Summer Olympic Games.

---

## Problem Description

For the first time at the Paris Olympics, men were eligible to compete in Artistic Swimming. As the coach of an artistic swimming club, you are tasked with designing formations using both male and female athletes.

You plan to form multiple trios among all athletes. Each trio must consist of:
- 1 male and
- 2 females.

To maximize aesthetics and coordination, the male in each trio must be **strictly taller** than both females.

Given the heights of `n` males and `m` females, determine the **maximum number of trios** that can be formed under these constraints.

---

## Input

- The first line contains two integers `n` and `m` — the number of male and female athletes, respectively.
- The second line contains `n` integers — the heights of the male athletes.
- The third line contains `m` integers — the heights of the female athletes.

---

## Output

- Output a single integer — the maximum number of trios that can be formed.

---

## Example

### Input 1
```
3 5
10 20 30
1 10 20 30 40
```

### Output 1
```
1
```

### Input 2
```
2 4
5 9
1 2 6 7
```

### Output 2
```
2
```

---

## Constraints

- For 50% of the test cases: `n, m ≤ 1000`
- For 100% of the test cases: `n, m ≤ 1,000,000`
- Heights are integers within the range `[1, 10^9]`

---

## Notes

- A trio is valid only if the male is taller than **both** females.
- Each athlete can be used at most once.
- Optimal formations should maximize the number of such valid trios.

---

## Fun Fact

Artistic swimmers are among the best-conditioned athletes in the world, undergoing strength workouts, aerobic conditioning, flexibility exercises, and countless hours of practice to achieve peak performance.

---
