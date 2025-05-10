# Select Courses

**Input file:** standard input  
**Output file:** standard output  
**Time limit:** 1 second  
**Memory limit:** 1024 megabytes  

A new quarter is going to start. All students in UCR are working on registering new courses.  
There are `n` courses in total. The `i`-th course has credit `ci` (labeled from `1` to `n`). For these courses, some of them have prerequisite courses. A course can have zero or one prerequisite course. If you want to take a course, you have to take its prerequisite course at the same time. Assume you haven’t taken any of these `n` courses before.

For any student, the maximum number of courses to enroll in is `m`. You want to maximize the total credit you can get by selecting `m` courses while not violating the prerequisite rule. Below is an example.


| **Course ID** | **Prerequisite Course** | **Credit** |
|-----------|---------------------|--------|
| 1         | none                | 1      |
| 2         | 1                   | 1      |
| 3         | 2                   | 3      |
| 4         | none                | 3      |
| 5         | 2                   | 4      |



## Input

The first line contains two integers `1 ≤ n ≤ 300` and `1 ≤ m ≤ n`.  
The following `n` lines describe the `i`-th course. There are two numbers in the `i`-th line: `pi`, which is the prerequisite course id of this course, and `ci`, which is the credit of this course. If there’s no prerequisite course for a course `i`, `pi = 0`.  
Each `ci` is between 1 and 10.  
Note that the courses are labeled from `1` to `n`.

## Output

The output only contains one integer, which is the largest credit you can get.

## Examples

| **standard input** | **standard output** |
|--------------------|---------------------|
| 7 4                | 13                  |
| 2 2                |                     |
| 0 1                |                     |
| 0 4                |                     |
| 2 1                |                     |
| 7 1                |                     |
| 7 6                |                     |
| 2 2                |                     |

---

| **standard input** | **standard output** |
|--------------------|---------------------|
| 10 5               | 28                  |
| 0 4                |                     |
| 0 6                |                     |
| 1 2                |                     |
| 0 1                |                     |
| 2 8                |                     |
| 4 9                |                     |
| 3 7                |                     |
| 5 1                |                     |
| 8 2                |                     |
| 2 4                |                     |
