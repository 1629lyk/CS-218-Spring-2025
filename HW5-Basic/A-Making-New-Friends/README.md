# A. Making New Friends

**Time Limit:** 2 seconds  
**Memory Limit:** 256 megabytes

This is the first class of CS142. All the students are sitting in the classroom with `r` rows and `c` columns. Yihan wants the students to talk to each other such that they make friends with each other. As long as a student A talks to B, they become friends. However, this is the first class, and the students are very shy. A student will only make friends with another student that is adjacent to him/her. In other words, a student wants to make at most four friends. For students sitting on the boundary or corner, it is only 3 or 2.

When two students become friends, they share with each other everything they know. Yihan wants them to be friends because she wants to make course announcements easily. That is, when she makes an announcement later, she could just tell any one of the students, and the announcement will propagate to their friends, their friends' friends, ..., and finally all the students in the class can know. Apparently, she doesn't need all the students to be friends with each other.

But as mentioned, the students are very shy. Each of them has a shyness which is indicated by an integer. The good news is that, Yihan could use her candies. In particular, for a student A with shyness `S_A`, she can give some candies to A, and ask A: can you talk to B? Note that B has to be adjacent to A. As long as the number of candies is no smaller than the shyness `S_A` of A, A will agree (so the shier a student is, the more candy you need to let him/her talk). Although students are shy, they are very polite. If A talks to B, B will not refuse to talk, and they will become friends. Note that if Yihan wants a student to talk to multiple other students, she has to pay the corresponding number of candies multiple times.

Yihan wants to know the minimum number of candies she should prepare, such that by giving out candies, she can build some friendship connections between the students, and then she can make announcements easily—say, she could tell any of the students, and the announcement will be propagated to the whole class.

## Input

The first line contains two numbers `r` and `c` (1 ≤ `r`,`c` ≤ 10³), which is the number of rows and columns in the classroom. The classroom is full of students.

The next `r` lines each contain `c` numbers, the number on the `(i+1)`-th row and `j`-th column is the shyness of the student sitting at position `(i,j)` in the classroom.

## Output

The output contains only one number, which is the least number of total candies Yihan needs to give the students, such that she can make announcements easily.

### Example

**Input**
```
3 4
3 5 2 1
7 3 4 8
1 6 5 7
```

**Output**
```
26
```

## Note

`1 ≤ r, c ≤ 1000`.  
The shyness is a positive integer within 200.

![friendship-candy-distribution](https://espresso.codeforces.com/b18352c7d7d51803be977e2b887adfc175ce56d5.png)

The picture above shows how Yihan should distribute the candies in the sample input. An arrow from A to B means that A will receive candies and talk to B to make friends with B. The number next to each student is the number of candies he/she receives in total. In total Yihan needs 6+4+2+3+4+2+5 = **26** candies.
