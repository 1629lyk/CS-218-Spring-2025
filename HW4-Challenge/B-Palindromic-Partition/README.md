# B. Palindromic Partition

**Time Limit per Test:** 1 second  
**Memory Limit per Test:** 256 megabytes  



## Problem Statement

Let 𝑠 be a given string of up to 10⁶ digits. Find the maximal 𝑘 for which it is possible to partition 𝑠 into 𝑘 consecutive contiguous substrings, such that the 𝑘 parts form a palindrome.  

More precisely, we say that strings 𝑠₁, 𝑠₂, …, 𝑠ₖ form a palindrome if 𝑠ᵢ = 𝑠ₖ₋ᵢ₊₁ for all 1 ≤ 𝑖 ≤ 𝑘.



## Input

- The first line contains one integer 𝑡 (1 ≤ 𝑡 ≤ 10⁴) – the number of test cases.  
- Each test case consists of a line that contains a nonempty string of digits 𝑠 (1 ≤ |𝑠| ≤ 10⁶).  
- It is guaranteed that the sum of |𝑠| does not exceed 10⁶.



## Output

For each test case, print the maximal value of 𝑘 on a single line.



## Example

### Input
```
4
179791
42427114224
123456789
172794416896459447271
```

### Output
```
4
7
1
11
```



## Note

In the first sample case, we can split the string `179791` into 4 parts as `1 | 79 | 79 | 1`, and these parts together form a palindrome. It turns out that it is impossible to split this input into more than 𝑘 parts while still making sure the parts form a palindrome.
