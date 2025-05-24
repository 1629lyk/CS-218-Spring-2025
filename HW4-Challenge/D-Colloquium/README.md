# D. Colloquium

**Time Limit:** 1 second  
**Memory Limit:** 256 megabytes

The Computer Science department keeps getting larger, and our department has more and more undergraduate students and graduate students every year. Eventually, the department decided to partition CS 287: Colloquium in Computer Science, into two sections since otherwise no classroom is big enough for all students.

Yihan is running CS 287 now. Yihan has lots of experience on running the colloquium. She categorized the speakers based on their research areas: theory, system, and AI. The students don't like to attend talks in the same category consecutively. More precisely, the students will consider this talk and the two previous talks (or fewer if there haven't been that many), and:

- If they are in same category, students will only pay attention to the talk for **20 minutes**.
- If they are from two categories, students will pay attention to the talk for **40 minutes**.
- If they are all from three different categories, students will pay attention to the talk for the entire **60 minutes**.

Yihan has contacted `n` prominent computer scientists to give the talks. Of course, the speakers are busy, so they have committed a certain day to give the talk. Yihan knows the order, and her task is to determine which speaker should go to which section. The speakers do not like to give the same talk twice, so Yihan can only assign him/her to one of the sections.



## Input

- The first line contains an integer `n` (1 ≤ n ≤ 100,000).
- The second line contains a string consisting of `n` characters, indicating the speakers' research areas in the order of their talks. Each character will be one of the uppercase letters `'T'` (for theory), `'S'` (for system) or `'A'` (for AI).



## Output

- The output contains only one number: the total time (in minutes) that the students will pay attention to for both sections. The two sections can have different numbers of speakers.



## Examples

### Input
```
6
TSTAAS
```

### Output
```
240
```

### Input
```
16
TTSTSSSSTTTTTSTS
```

### Output
```
580
```