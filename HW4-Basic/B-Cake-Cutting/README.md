# B. Cake Cutting

**Time limit per test:** 1 second  
**Memory limit per test:** 512 megabytes  

Preston has been taking a lot of baking classes, so today he decided to bake a cake. Just as Preston finished decorating the cake, Celvin came and wanted some of it too.

The cake can be thought of as a circle. Each piece has a size Aᵢ, but since Preston has not mastered the art of cutting cakes, all of the pieces turned out to be different sizes.

![Cake Cutting Diagram](https://espresso.codeforces.com/ddf1cb9a115629703b2c33298a2de2fed009a1eb.png)

Because the slices are uneven, they decided to split the cake according to the following rules:

- First, Preston gets to choose **any** slice from the cake.
- Next, starting with Celvin, they each take turns taking a slice.
- However, a player is only allowed to take a piece if **one of the neighboring pieces has already been taken**.
- Celvin always takes the **largest available slice** that he can access at the time.

Your task is to determine:  
**What is the maximum total amount of cake that Preston can get?**



## Input

The first input will be an integer `n` (1 ≤ n ≤ 2000),  
the number of slices that the cake is cut into.

Then follow `n` lines, where each line contains an integer Aᵢ (1 ≤ Aᵢ ≤ 10⁹),  
the size of the i-th slice.

It is guaranteed that all Aᵢ values are **distinct**.



## Output

Output a single integer — the maximum total amount of cake that Preston can get.



## Examples

### Input
```
5
2
8
1
10
9
```

### Output
```
18
```



### Input
```
8
1
10
4
5
6
2
9
3
```

### Output
```
26
```



## Explanation

**First Test Case:**

- Preston takes the 2nd slice (value = 8)  
- Celvin takes the 1st slice (value = 2)  
- Preston takes the 5th slice (value = 9)  
- Celvin takes the 4th slice (value = 10)  
- Preston takes the 3rd slice (value = 1)

Total for Preston: 8 + 9 + 1 = **18**