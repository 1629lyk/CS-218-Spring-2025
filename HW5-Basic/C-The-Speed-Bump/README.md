# C. The Speed Bump

**Time Limit:** 1 second  
**Memory Limit:** 256 megabytes

**Sheldon:** (Knock, knock, knock) Penny, (knock, knock, knock) Penny, (knock, knock, knock) Penny, ...

**Penny (opening door):** Sheldon, what is it?

**Sheldon:** Leonard's asleep.

**Penny:** Thanks for the update (begins to close door.)

**Sheldon:** No, wait. You have to drive me to work.

**Penny:** Oh, dear God.

**Sheldon:** I'm sorry, I didn't realize I was interrupting your morning prayers. When you're done, we'll go.

*(Scene: Inside Penny's car.)*

**Sheldon:** You're going up Euclid Avenue? Leonard takes Los Robles Avenue.

**Penny:** Well, good for Leonard.

**Sheldon:** Euclid Avenue is shorter as the crow flies, but it has speed bumps, which appreciably increase point-to-point drive time, making it the less efficient choice. ... (car went through a speed bump and they bumped up and down) Of course, if you're not going to slow down for the speed bumps, I withdraw my previous objection.

— *The Big Bang Theory, S2E5*

---

In S2E5, Penny drove Sheldon to work. Sheldon observed that Penny was using a different route than Leonard's regular route to the university. He pointed out that although Penny's route is shorter in distance, it may go through more speed bumps, so it may slow down the overall time, and was obviously less comfortable.

Sheldon hated speed bumps. He wanted to figure out if he could avoid speed bumps as much as he could. He found the map in LA, which contains all relevant roads represented as a graph. He also marked all roads with speed bumps. He wanted to find a route from home to the university to minimize the number of speed bumps on the way. When there were multiple such routes, he wanted to find the one with the shortest distance.

---

## Input

The first line of the input contains two integers `n` and `m`, where:

- `n` is the number of locations on the map,
- `m` is the number of roads connecting the locations.

The locations are labeled from `0` to `n−1`.  
Sheldon's home is always at location `0`, and the university is always at location `n−1`.  
It is guaranteed that the two locations are connected with each other.

The next `m` lines each describe a road. Line `i` contains four integers `a_i`, `b_i`, `c_i`, `d_i`.  
It means that road `i` connects locations `a_i` and `b_i`, it has `c_i` speed bumps on the way, and its length (distance) is `d_i`.

- Constraints:
  - `0 ≤ a_i, b_i ≤ n−1`
  - `0 ≤ c_i ≤ 5`
  - `0 < d_i ≤ 100`

All roads are **bi-directional**.

---

## Output

The output contains two integers `x` and `y`:

- `x`: the smallest number of speed bumps on the path from home to university.
- `y`: the shortest distance among all such paths that have `x` speed bumps.

---

## Examples

### Example 1

**Input**
```
2 1
0 1 0 10
```

**Output**
```
0 10
```

---

### Example 2

**Input**
```
6 7
0 1 2 10
0 3 1 10
1 3 1 10
1 2 1 10
3 4 1 10
4 5 2 20
2 5 1 10
```

**Output**
```
4 30
```

---

### Example 3

**Input**
```
7 9
0 1 2 10
0 3 1 10
1 3 1 10
1 2 1 10
3 4 1 10
4 6 2 20
2 6 1 10
0 5 1 100
5 6 1 100
```

**Output**
```
2 200
```

---

## Note

- `1 ≤ n ≤ 10^5`  
- `1 ≤ m ≤ 2 × 10^5`  
- `0 ≤ c_i ≤ 5`  
- `0 < d_i ≤ 100`

---

This problem can be solved using a modified version of Dijkstra's algorithm, where each node stores a pair (bumps, distance) and prioritization is done lexicographically. This ensures optimal routing with minimal speed bumps and shortest distance among those paths.
