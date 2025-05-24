# C. Happy dog, happy life

**Time Limit per Test:** 1 second  
**Memory Limit per Test:** 256 megabytes

You probably know that, dogs are always tired of old toys and want new ones. For this reason, there are a lot of "advent calendars" as dog toys for sale. In particular, an advent calendar for a dog means a list of toys associated with dates, and on each day, a new toy will be revealed, and you can just give it to your dog. An example is available here.

Yihan just bought such an advent calendar for her dog. She knew that, to the dog, each toy has a "funness", which is how fun the dog rates it. However, she knew that the dog is very picky - he won't want a toy that is worse (less fun) than the previous ones. As a result, Yihan decided to just skip some of the toys to make sure that the dog is always getting toys that are strictly better and better. If the dog can get better and better toys, he is OK with waiting a few days and playing with the old ones, as long as the total "happiness" (defined below) can be high.

The happiness of the dog on day 𝑖 is the total funness of toys he has on that day. The total happiness of the dog, is the sum of happiness of all days for the dog. Now, given the list of toys based on their ordering on the calendar, and their funness, your task is to help Yihan compute, what is the highest happiness the dog can have.



## Input

The first line is an integer 𝑛, which is the total number of toys in the advent calendar.

The next line contains 𝑛 integers. The 𝑖-th integer is the funness of the 𝑖-th toy.



## Output

The output is one integer, which is the highest happiness the dog can have.



## Examples

### Input
```
5
15 3 4 5 20
```

### Output
```
95
```

### Input
```
8
13 17 26 14 8 15 12 16
```

### Output
```
379
```

### Input
```
10
7 8 3 5 6 1 4 10 9 2
```

### Output
```
172
```



## Note

In the first example, Yihan can give the dog the toys on days 1 and 5, so the dog will get 2 toys with happiness on each day as:

15, 15, 15, 15, 35

And the total happiness is 95.

She can also give the dog toys on days 2, 3, 4, and 5. Although in this case, the dog will get 4 toys, the happiness on each day is:

0, 3, 7, 12, 32

And the total happiness is 54.

As the result, the best solution is 95.



## Constraints

- For 50% of the inputs, 𝑛 ≤ 10³  
- For 100% of the inputs, 𝑛 ≤ 10⁵  
- All input funness values are within 10⁶  
- Please use a 64-bit integer for your final answer.
