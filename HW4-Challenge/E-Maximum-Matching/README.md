# E. Maximum Matching

**Time limit per test:** 2 seconds  
**Memory limit per test:** 256 megabytes  

Today you will be going skiing on a piste consisting of 𝑛 segments, where you travel in order from segment 1 to 2 ... to 𝑛. In each segment, you can perform one ski trick represented by a lowercase letter a through z. You don't have to perform the trick if you don't want to.

There is a Skiing Contest for Computer science (SCCs) where contestants attempt to do tricks in a way that they are accepted by a regular expression.

## Regular Expression Format

The regular expression consists of 𝑚 characters with the following properties:

- Each expression consists of the lowercase letters `a` through `z` and the characters `?`, `*`, `[`, `]`, `(`, `)`
- Each letter matches a trick corresponding to that letter.
- The question mark `?` matches any trick.
- The brackets `[` and `]` are always correctly paired. Inside them are only lowercase letters. A pair of brackets and the letters inside match any single trick that matches any letter inside the brackets.
- The asterisk `*` indicates that the preceding sequence – a letter, a question mark, brackets `[]`, or a portion of the expression enclosed in parentheses `()` – may be repeatedly matched any amount of times. The number of repetitions may be zero.
- Parentheses `(` and `)` are always correctly paired and are always immediately followed by an asterisk. Inside the parentheses, there is an expression with the same properties listed above, but it does not contain parentheses.

## Problem Definition

A **routine** is a sequence of tricks that can be performed while traveling through the piste.

A **matching routine** is a routine whose sequence of tricks matches the regular expression.

A **maximum matching routine** is a matching routine such that there are no matching routines with more tricks.

**Objective:** Determine how many tricks are in a maximum matching routine. If no matching routines exist, print `-1`.



## Input

Each test contains multiple test cases. The first line contains the number of test cases 𝑡 (1 ≤ 𝑡 ≤ 1000). The description of the test cases follows.

Each test case contains:

1. An integer 𝑛 (1 ≤ 𝑛 ≤ 1000) – the number of segments.  
2. A string 𝑠 (|𝑠| = 𝑛) – the trick you can perform for each segment.  
3. An integer 𝑚 (1 ≤ 𝑚 ≤ 1000) – the length of the regular expression for matching.  
4. A string 𝑝 (|𝑝| = 𝑚) – the regular expression for matching.



## Output

For each test case, output the number of tricks in the maximum matching routine, or `-1` if no matching routine exists.



## Example

**Input**
```
4
3
aba
2
a\*
9
algorithm
6
design
4
food
13
(\[ba]g??t*e)*
20
candycandycandycandy
14
\[abc]*(andy)*?
```

**Output**
```
2
-1
0
14
```

