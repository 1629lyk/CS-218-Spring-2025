
# A. Lazy Piano

**time limit per test**: 1 second  
**memory limit per test**: 256 megabytes

Takahashi has a piano with 𝑘 keys arranged in a row. The 𝑖th key from the left is called key 𝑖.

He will play music by pressing 𝑛 keys one by one. For the 𝑖th press, he needs to press key 𝑎𝑖 using his left or right hand.

Before starting to play, he can place both of his hands on any keys he likes, and his fatigue level at this point is 0. During the performance, if he moves one hand from key 𝑥 to key 𝑦, the fatigue level increases by |𝑦−𝑥| (conversely, the fatigue level does not increase for any reason other than moving hands). To press a certain key with a hand, that hand must be placed on that key.

Find the minimum possible fatigue level at the end of the performance.

## Input

Each test contains multiple test cases. The first line contains the number of test cases 𝑡 (1 ≤ 𝑡 ≤ 10³). The description of the test cases follows.

The first line of each test case contains two integers 𝑛, 𝑘 (1 ≤ 𝑛, 𝑘 ≤ 5⋅10³) – the number of presses for the song and number of keys on the piano, respectively.

The second line of each test case contains 𝑛 integers 𝑎₁,…,𝑎ₙ (1 ≤ 𝑎ᵢ ≤ 𝑘) – the keys to be pressed for the song.

Additionally, the sum of 𝑛 over all test cases doesn't exceed 5⋅10³.  
Additionally, the sum of 𝑘 over all test cases doesn't exceed 5⋅10³.

## Output

For each test case, output a single integer – the minimum possible fatigue level at the end of the performance.

## Example

### Input
```
4
4 7
1 3 5 7
4 10
1 10 1 10
6 10
1 10 2 9 3 8
8 100
22 75 26 45 72 81 47 29
```

### Output
```
4
0
4
55
```
