# C. Number Candles

**Time Limit:** 0.5 seconds  
**Memory Limit:** 256 megabytes

---

## Problem Description

You may know that there are birthday candles shaped like numbers.  
For example, if Yihan is celebrating her 18th birthday, she can buy two candles, "1" and "8", and put them on the cake.

The price for each number candle is different. In particular, the price for number `i` is `p_i` dollars.  
The store has **run out of the number "0"**, so you cannot buy a zero candle.

Yihan now has **M** dollars.  
Using M dollars, she wants to buy number candles to create the **largest possible number**.

---

## Input

- The first line contains one integer `M` (`M < 10^5`), the amount of money Yihan has.
- The second line contains 9 integers, representing the prices of number candles `1` to `9`.  
  (Each price is no more than `10^5`.)

It is guaranteed that you can buy at least one candle.

---

## Output

- Print a single integer — the **largest number** Yihan can create by using her M dollars.

---

## Example

### Input 1
```
10
4 3 10 8 5 6 3 12 4
```
### Output 1
```
977
```

---

### Input 2
```
28
7 5 6 8 5 5 6 10 7
```
### Output 2
```
97666
```

---

### Input 3
```
50
1 1 1 1 1 1 1 1 1
```
### Output 3
```
99999999999999999999999999999999999999999999999999
```

---

### Input 4
```
48
10 10 12 19 13 16 19 21 22
```
### Output 4
```
6322
```

---

### Input 5
```
100
11 12 13 14 15 16 17 18 19
```
### Output 5
```
211111111
```

---

## Notes

- Time limits: **1 second**.
- For **50%** of the test cases, **M ≤ 20**.
- For **100%** of the test cases, **M ≤ 10^5**.

---