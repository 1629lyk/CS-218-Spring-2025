# A. Symmetry Makes Perfect

**Time Limit per Test:** 1 second  
**Memory Limit per Test:** 256 megabytes

## Problem Statement

Yihan is shopping for candies for her student again, and this time she wants something new. Because Yihan has spent a lot of money at the candy store, the owner of the store decided to give Yihan a candy string for free. A candy string is a string of candies (of course), each of a different flavor.

There is one candy string that was made up by the salesman already in the store. There are also bulks of single candies of each flavor (say, an infinite number for each). The price for different flavor is also different. Suppose the price of flavor 𝑥 is 𝑝[𝑥].

Yihan likes the idea of candy string. However, she doesn't like the particular candy string in the store, because it is not symmetric. For example, if there are four flavors 𝑎, 𝑏, 𝑐 and 𝑑, a candy string of 𝑎𝑏𝑐𝑑𝑐𝑏𝑎 or 𝑎𝑎𝑏𝑏𝑎𝑎 is symmetric, while 𝑎𝑏𝑐𝑑𝑎𝑏𝑐𝑑 or 𝑎𝑎𝑎𝑏 is not.

Yihan wants to DIY a new candy string based on the current candy string she has. However she was told that, she needs to pay for the extra cost to make it symmetric. She is okay with that because she just cannot tolerate it to be asymmetric. In particular, she will insert some candies into the candy string to make it symmetric. To insert a candy with a certain flavor anywhere in the candy string, Yihan has to pay the price of the inserted flavor.

Yihan won’t delete or replace any candy from the string since it’s already free. She wants to know the minimum amount she needs to pay to make the candy string symmetric.


## Input

- The first line contains two integers: 𝑛 (1 ≤ 𝑛 ≤ 10³) and 𝑘 (1 ≤ 𝑘 ≤ 26)  
  𝑛 is the length of the candy string, and 𝑘 is the number of flavors.  
  Only the first 𝑘 lowercase letters of the alphabet will appear in the string and can be used for insertions.

- The next 𝑘 lines each contain a single integer:  
  The (𝑖+1)-th line represents 𝑝[𝑖], the price of inserting flavor 𝑖 (1 ≤ 𝑝[𝑥] ≤ 10³)

- The last line contains 𝑛 lowercase characters, the initial flavor string.



## Output

Print a single integer — the minimum cost Yihan needs to pay to make the candy string symmetric.



## Examples

### Input
```
3 2
5
1
abb
```

### Output
```
2
```



### Input
```
5 4
1
2
3
4
abcad
```

### Output
```
6
```



### Input
```
10 8
2
5
6
1
3
5
4
3
hahahahaha
```

### Output
```
2
```



### Input
```
7 26
1
2
3
4
5
6
7
1
2
3
4
5
6
7
1
2
3
4
5
6
1
2
3
4
5
6
popping
```

### Output
```
16
```



### Input
```
8 26
1
1
1
1
1
1
100
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
kayaking
```

### Output
```
7
```



### Input
```
8 26
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
kayaking
```

### Output
```
3
```



## Note

**Example 1:**  
There are several ways to make it symmetric. For example, Yihan could spend 5 dollars to add an `'a'` at the end. However, the cheapest way is to add two flavor `'b'` candies at the beginning, costing 2.

Greedy strategies may not always lead to the optimal solution. Use dynamic programming for guaranteed correctness.