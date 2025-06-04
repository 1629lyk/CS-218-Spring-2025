# B. Moving Stairs

**Time limit per test:** 1 second  
**Memory limit per test:** 256 megabytes  

There were a hundred and forty-two staircases at Hogwarts: wide, sweeping ones; narrow, rickety ones; some that led somewhere different on a Friday; some with a vanishing step halfway up that you had to remember to jump. Then there were doors that wouldn't open unless you asked politely, or tickled them in exactly the right place, and doors that weren't really doors at all, but solid walls just pretending. It was also very hard to remember where anything was, because it all seemed to move around a lot. The people in the portraits kept going to visit each other and Harry was sure the coats of armor could walk.

— Rowling, J.K.. *Harry Potter and the Philosopher's Stone.*

---

In Hogwarts, the staircases are always moving. In particular, in the castle, each stairway connects two platforms: one end is a fixed platform, and the other end changes between two possible platforms all the time. There are 𝑛 platforms in Hogwarts, which are labeled with numbers 0 to 𝑛−1. There are 𝑚 bi-directional stairways connecting them. The stairways move every minute. Each stairway can be labeled by three integers (𝑥, 𝑦, 𝑧). It means that at even timestamps (0, 2, 4, ...), the stairway connects two platforms 𝑥 and 𝑦; at odd timestamps (1, 3, 5, ...), the stairway connects platforms 𝑥 and 𝑧. You can check out how the stairs move here and here.

When Harry Potter was in his first year, he got lost many times in the castle and had been late for many classes. After some survey, he found the information for all stairways. Now he wanted to know the quickest way to go to a certain destination.

The time Harry needed to run up or down the stairway 𝑖 (from one platform to the other end) is 1 unit of time. For example, consider a stairway with label (𝑥, 𝑦, 𝑧). At timestamp 0, if Harry was at platform 𝑥, then Harry could step onto that stairway. He would arrive at platform 𝑧 at timestamp 1. Similarly, at timestamp 1, if Harry was at platform 𝑥, then Harry would arrive at platform 𝑦 at timestamp 2. Another trick is that, if at timestamp 0, Harry was at platform 𝑦, he could step onto the stairway, and in the next timestamp, he could also arrive at platform 𝑧 - he could just stay on the stairway and wait until the stairway took him to platform 𝑧. Harry could also stay for a while on the platforms to wait for a certain stairway to come.

For simplicity, the platform of Gryffindor Common Room is always labeled as platform 0. When he started at Gryffindor Common Room, it was timestamp 0 (an even timestamp). You need to compute the earliest time he could arrive at a certain platform 𝑘.

![A stairway moving while Harry Potter was still on it.](https://espresso.codeforces.com/81d94092b344a8c7a338e9e8f202ff4f2ccf6b14.png)  
*A stairway moving while Harry Potter was still on it.*

---

## Input

The first line contains three integers. The first integer 𝑛 is the number of platforms. The second integer 𝑚 is the number of stairways. The third integer 𝑘 is the destination platform Harry wanted to go to.

The next 𝑚 lines each contain four integers 𝑥ᵢ, 𝑦ᵢ, and 𝑧ᵢ. This means the 𝑖-th stairway will be connecting platforms 𝑥ᵢ and 𝑦ᵢ at even timestamps (0, 2, 4, ...), and will be connecting platforms 𝑥ᵢ and 𝑧ᵢ at odd time stamps (1, 3, 5, ...).

## Output

The output only contains one integer, which is earliest time Harry can arrive at platform 𝑘, if possible.

If it's impossible to arrive at platform 𝑘 from Gryffindor Common Room (platform 0), then please output -1. You probably need to use some secret passages to get there.

---

## Examples

**Input**
```
6 4 5
0 1 2
3 2 1
4 2 3
5 3 4
```

**Output**
```
4
```

**Input**
```
10 8 9
0 3 1
1 2 3
2 4 5
3 6 4
6 8 5
8 7 9
4 5 7
7 8 9
```

**Output**
```
5
```

---

## Note

For 50% of the test data, 𝑛 ≤ 100, 𝑚 ≤ 1000.

For 100% of the test data, 𝑛 ≤ 10^5, 𝑚 ≤ 2 × 10^5.

### Example 1:

Their fastest path is shown as follows:

- At time 0, use the stairway (0,1,2). When he arrives at the other end of the stairway, it is time 1, and the destination is platform 2.  
- At time 1 (at platform 2), wait at platform 2.  
- At time 2 (still at platform 2), use the stairway (4,2,3). This stairway is now connecting 2 and 4. He will arrive at platform 4 after 1 unit of time.  
- At time 3 (arriving at platform 4), use the stairway (5,3,4). This stairway is now connecting 4 and 5. He will arrive at platform 5 after 1 unit of time.  
- At time 4, arriving at platform 5.  
- The output should be 4.

### Example 2:

Their fastest path is shown as follows:

- At time 0, use the stairway (0,3,1). When he arrives at the other end of the stairway, it is time 1 (odd), and the destination is 1.  
- At time 1 (arriving at platform 1), use the stairway (1,2,3). When arriving at the other end, it is time 2 (even), and the destination is 2.  
- At time 2 (arriving at platform 2), use the stairway (2,4,5). When arriving at the other end, it is time 3 (odd), and the destination is 5.  
- At time 3 (arriving at platform 5), use the stairway (6,8,5). This stairway is now connecting 6 and 5. Harry can step onto this stairway. In the next timestamp, the stairway will take him to platform 8.  
- At time 4 (arriving at platform 8), use the stairway (8,7,9). When arriving at the other end, it is time 5, and the destination is 9.  
- At time 5, arriving at platform 9.  
- The output should be 5.

---

## An Unimportant Note

In the first several movies, the stairs are shown to be constantly moving (as described in this problem). Surprisingly, that was never mentioned in the novels (in later movies, this setting was also changed). However, probably because the first several movies were very successful, many people still believe that's how the stairs work in Hogwarts.
