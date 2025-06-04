# C. Catch the theft!

**Time Limit:** 1 second  
**Memory Limit:** 256 megabytes

---

The City of Riverside Police Department hired Yihan as an assistant detective and help with a variety of issues as a computer scientist. After helping the police for a few months, Yihan plans to develop several software programs so that she can save more time to teach at UCR, especially CS 218.

One of the applications that is especially useful is to assign checkpoints. Often time, a theft stole in place A and wanted to go to place B. In this case, if the police set some checkpoints and block all possible paths, then catching the theft becomes much easier. Usually in this case, Yihan's job is to provide the police a list of checkpoints. Since this is a relatively common task, this is one of Yihan's programs she wants to design. Another reason is that an efficient algorithm can compute the solution much faster than doing it by hand.

The City of Riverside has many roads connected by crossroads. We denote the number of roads as 𝑚 and the number of crossroads as 𝑛. We also know Place A and Place B, which are two crossroads. The police want to put checkpoints on a subset of the roads that disconnects Place A and Place B. Since each road is different, the number of police vehicles to block the road is different. We want to compute the minimum total number of police vehicles for this task. Yihan realized that this task can be solved using the algorithms covered in CS 218, so she also made it a homework problem so you can try to solve it as well.

---

## Input

The first line contains four integers 𝑛 and 𝑚, 𝐴, and 𝐵 (1 ≤ 𝐴, 𝐵 ≤ 𝑛).  
Each of the next 𝑚 lines contains three integers 𝑢, 𝑣, and 𝑐, indicating the 𝑖-th road is between crossroad 𝑢 and 𝑣, and requires 𝑐 police vehicles to set up a checkpoints.  
All roads are bidirectional.

---

## Output

The output contains a single integer, indicating the minimum number of police vehicles to disconnects Place A and Place B.

---

## Example

**Input**
```
6 8 1 6
1 2 4
1 3 3
2 3 2
2 4 4
3 5 2
4 5 1
4 6 2
5 6 4
```

**Output**
```
5
```

---

## Note

2 ≤ 𝑛 ≤ 10^4  
1 ≤ 𝑚 ≤ 10^5
