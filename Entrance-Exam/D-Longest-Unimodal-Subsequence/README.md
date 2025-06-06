# D. Longest Unimodal Subsequence

**Time limit per test:** 0.5 seconds  
**Memory limit per test:** 256 megabytes  

---

In class, we talked about how to compute the longest increasing subsequence, and in the entrance exam, we tried to compute the longest decreasing subsequence.  
In this problem, you are going to write a program to compute the **Longest Unimodal Subsequence (LUS)** of a sequence.  

In particular, for a sequence \( a_1, a_2, a_3, \dots, a_n \), a unimodal subsequence is a sequence

\[
a_{i1}, a_{i2}, \dots, a_{im}
\]

where \( 1 \leq i_1 < i_2 < \dots < i_m \leq n \), and there exists some \( 1 < k < m \) such that:

\[
a_{i1} < a_{i2} < \dots < a_{ik} > a_{ik+1} > \dots > a_{im}
\]

For example:
- A sequence `1, 2, 3, 4, 3, 2, 1` is unimodal 
- A sequence `4, 3, 2, 1` is **not unimodal** 

---

## Problem Statement

We want to find the **longest** such unimodal subsequence.  
You only need to output the **length** of the LUS.

---

## Input

- The first line contains one integer \( n \) \( (1 \leq n \leq 1000) \).
- The second line contains \( n \) integers, representing the sequence \( a_i \).
- Each \( a_i \) is in the range \([0, 10^6]\).

---

## Output

- Output only one integer: the **length** of the longest unimodal subsequence.

---

## Examples

### Input
```
9
1 5 4 7 9 6 3 8 2
```
### Output
```
7
```

---

### Input
```
6
176486 838902 354360 156737 698300 64483
```
### Output
```
5
```

---

### Input
```
6
54557 830719 387307 588299 906303 371374
```
### Output
```
5
```

---

### Input
```
10
684819 461753 14555 10687 439796 279026 9629 331527 987012 31686
```
### Output
```
5
```

---

### Input
```
12
190766 588802 342038 472303 854909 537524 489480 449393 749430 957344 165790 480370
```
### Output
```
8
```

---