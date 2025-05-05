# C. Gridiron Gauntlet

**Time limit per test:** 0.5 s  
**Memory limit per test:** 256 megabytes  

Stay in it to the end!  
Get tackled one time and you're out!

Gridiron Gauntlet is a 4-player minigame in Super Mario Party, and you can view how the game is actually played [here](https://www.mariowiki.com/Gridiron_Gauntlet). The game is played on a 5×5 grid where each row and column is given a number from 1 to 10 as in the picture below. We will call each of these rows/columns a track. At each unit of time, at most 10 Chargin' Chucks can appear each taking up a single track. (In the original game, the Chargin' Chucks can come from three directions, so at most 15 ...

If a Chargin' Chuck appears on a track x at some time t, it will move through the whole track, kicking out any player that is on the same track. For example, in the picture below, we have Chargin' Chucks moving through tracks 6, 8, and 10 at time 21. Because Wario (the character in purple) was in the middle column, he was kicked out by the Chargin' Chuck at track 8. Between each wave of Chargin' Chucks' attacks, each player can either stay at their current cell or move to an adjacent cell. For a cell ...

Given all the tracks that the Chargin' Chucks will appear and the time that they will do so, we want to know the maximum time that a player can stay alive. You are free to choose to start at any cell when the game begins (at time 0).


### Input

The first line of the input contains one integer, n (0 ≤ n ≤ 10^4), which is the number of Chargin' Chucks that will appear in the game.

The next n lines each contain two integers t, x (0 ≤ t < n, 1 ≤ x ≤ 10), which means that at time t, a Chargin' Chuck will appear at track x. They will be sorted by the time.


### Output

The output only contains one integer, which is the longest time one can survive in the game. If the player can survive until the end, you need to output t_max + 1, where t_max is the time when the last Chargin' Chuck appears.


### Example

#### Input
```
15
0 8
0 3
1 4
1 5
1 6
1 7
2 1
2 2
2 3
2 4
3 7
4 5
4 9
5 1
5 2
```

#### Output
```
2
```


### Note

For the first test case, at time 0 there are a lot of cells that will keep you alive. Note that at time 1, you have to stay at the 3×3 cells on the bottom right. However, at time 2, the only safe cells are those on the first row. Therefore, you cannot move to any safe cells at time 2, and the maximum time you can survive is just 2.

In the original game, you actually have three chances. In this problem, we use a simplified version and once you are tackled, you lose the game.

**Source of pictures and descriptions:**  
[https://www.mariowiki.com/Gridiron_Gauntlet](https://www.mariowiki.com/Gridiron_Gauntlet)
