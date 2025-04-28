
# Problem A: Finding the Minimum Value

**Time limit per test:** 0.5 seconds  
**Memory limit per test:** 256 megabytes

---

## Problem Statement

Your task for this problem is very simple: you are going to find the minimum value for the function:

\[
f(x) = \frac{x^2}{\ln{x}} + a \cdot x
\]

in the range \(1 < x < 2\), where \(a\) is a real number that will be provided in the problem.

---

## Input

The input contains one single real number \(a\).

---

## Output

The output contains a single real number, which is the minimum value of the function \(f(x)\) in the range \(1 < x < 2\).

The error of your answer must be within \(10^{-6}\).

---

## Examples

### Input
```
3
```

### Output
```
10.006560571
```

---

### Input
```
1.34
```

### Output
```
7.554532170
```

---

## Notes

- You should find the minimum of a **continuous, unimodal function** within a specified interval.
- Algorithms like **Ternary Search** or **Golden Section Search** are well suited for this task.
- Ensure precision by maintaining an absolute or relative error within \(10^{-6}\).
