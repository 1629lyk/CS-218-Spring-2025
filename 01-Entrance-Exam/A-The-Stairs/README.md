
# A. The Stairs

**Time limit per test:** 0.5 s  
**Memory limit per test:** 256 megabytes

> **Sheldon:** You want to hear an interesting thing about stairs?  
> **Leonard:** Not really.  
> **Sheldon:** If the height of a single step is off by as little as two millimeters, most people will trip.  
> **Leonard:** I don't care. Two millimeters? That doesn't seem right.  
> **Sheldon:** No, it's true, I did a series of experiments when I was twelve, my father broke his clavicle.  
> **Leonard:** Is that why they sent you to boarding school?  
> **Sheldon:** No, that was the result of my work with lasers.  
> __The Big Bang Theory, S1E1, Pilot Episode__

In S1E1, Sheldon told Leonard that just changing one step in the stairs by 2 millimeters may cause most people to trip. Sheldon had done such an experiment before, and his father broke his clavicle due to it.

To fully convince Leonard, Sheldon also changed the height of one step in the stairs in their building, and he bet that Leonard would trip at that step if he ran down the stairs. To win the bet, Leonard decided to first find where the special step is, so that he could be prepared when running to that step.

However, since the change was small, it's hard to tell which step was changed just by seeing them. Luckily, Leonard found a device from his lab that could give the absolute altitude of a position. Using the device, Leonard got the accurate altitude of all stairs.

Your task is to help Leonard find the special step. That is, if we fix the height of the incorrect step, then all adjacent steps will have exactly the same difference in height.

---

## Input

- The first line contains one integer `n`, the number of steps in the stairs.
- The next `n` lines each contain an integer, where the `i`-th integer is the altitude of the `i`-th stair, for `1 ≤ i ≤ n`.
- The heights can be in either ascending or descending order.

---

## Output

- Output a single integer `x`, which is the 1-based index of the step that was changed by Sheldon and has an incorrect height.

It is guaranteed that only **one step** in the stairs had been changed by Sheldon.

---

## Examples

### Input
```
8
1
2
3
4
4
6
7
8
```
### Output
```
5
```

### Input
```
5
10
20
31
40
50
```
### Output
```
3
```

### Input
```
6
1000
900
801
700
600
500
```
### Output
```
3
```

---

## Notes

- For 100% of the test data: `5 ≤ n ≤ 100`.
- The altitude of each step is a positive integer within `10^4`.

---

**This problem is modified from UCRPC F23.**
