# A. Weightlifting

**Time limit per test:** 1 second  
**Memory limit per test:** 256 MB  

This problem is from UCRPC, themed in 2024 Summer Olympic Games.

In this problem, you're going to help the weightlifting athletes assemble a set of weights on a barbell to match a specific target weight 𝑥. Each side of the barbell must be balanced with exactly half of the total target weight, 𝑥/2.

You have 𝑛 barbell plates, each with a known weight that is a multiple of 0.5. Your goal is to determine the minimum number of plates required to achieve the exact total weight 𝑥. Since the two sides must be balanced, you need to find two sets of plates, 𝑥/2 each. Each plate can be used at most once. You want to know the minimum number of barbell plates you need to achieve this.

If it's impossible to assemble the weights to meet the target, your program should indicate this with an output of -1.



## Input

The first line contains two integers: 𝑛 (the number of barbell plates) and 𝑥 (the desired total weight).  

The following 𝑛 lines each contain the weight of one barbell plate. Each weight is guaranteed to be a multiple of 0.5. They are labeled with 1 to 𝑛.



## Output

The first line should show 𝑘, which is the minimum number of barbell plates needed in total.

The second line should list the indices of the plates placed on the left side of the barbell.

The third line should list the indices of the plates placed on the right side.

The total weight of each side must be 𝑥/2, each plate can appear in at most one side.

**Note:** Make sure your output does not have trailing newline or whitespace.  
If there are multiple answers, you may output any of them.



## Example

**Input**
```
5 3
0.5 0.5 1.0 1.5 0.5
```

**Output**
```
3
3 5
4
```



## Note

- For 50% of the test data, 𝑥 is an even number, and all plates have integer weights.  
- For 30% of the test data, 𝑛≤20, 𝑥≤20.  
- For 100% of the test data, 𝑛≤200, 𝑥≤200, all plates weights are multiples of 0.5.



### Fun facts about weightlifting at the Olympic Games:

Weightlifting was one of the sports at the first modern Olympic Games in 1896 in Athens, Greece. However, women's weightlifting was added much later, making its debut at the 2000 Sydney Games. This inclusion marked a significant step towards gender equality in Olympic sports.
