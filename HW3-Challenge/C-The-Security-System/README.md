# C. The Security System

**time limit per test:** 1 second  
**memory limit per test:** 256 megabytes

> Howard: All right, we've got a titanium dead bolt and a reinforced jamb controlled by a state-of-the-art electronic access system.  
> Sheldon: What if they cut the power?  
> Raj: There's a 200-watt uninterruptible backup power supply.  
> Sheldon: What if someone steals my keys?  
> Raj: There are independent voice and fingerprint scanners.  
> Sheldon: What if someone kidnaps me, forces me to record my voice, and then cuts off my thumb?  
> Leonard: I'll send them a basket of muffins.  
> Howard: Now, inside, we've got motion detectors, infrared sensors, and cameras connected to a server running state-of-the-art facial recognition software.  
>
> — *The Big Bang Theory, S3E13, The Bozeman Reaction*

In S3E13, Sheldon and Leonard's apartment was broken into, and therefore Howard helped them install a full security system. The security system needed a bunch of sensors in the room to be deployed at one side of the room. They will send signals in a straight line to the other side of the room. As a result, there cannot be too many furnitures on the way, since they may block the signal.

Sheldon and Leonard's apartment can be viewed as a 𝐿×𝐿 grid. We use coordinate (𝑥,𝑦) to represent the position on the 𝑥-th row and 𝑦-th column for 1≤𝑥,𝑦≤𝐿. Each furniture may take some consecutive cells. For simplicity, let's consider each of them to be a vertical line of consecutive cells, from (𝑎,𝑏) to (𝑐,𝑑), and 𝑏=𝑑 is always true. There are 𝑛 furnitures. Below is an example of the apartment's furniture for 𝐿=9 and 𝑛=7.

![Furniture Blocking Diagram](https://espresso.codeforces.com/e4252f41adff7de61b55593d5fa84b0074362993.png)

The sensors are on the left side of the map. They send signals horizontally to the right side of the room. To make the sensors function properly, there can be at most 𝑘 "obstacles" on the way. For example, if 𝑘=3, then the picture above does not allow the sensors to work properly - for row 3 and row 7, there are four furnitures on the way.

To make the security system work, Sheldon and Leonard decided to remove some of the furnitures. Of course they want to keep as many current furnitures as possible, so they want to know the smallest number of furnitures that they need to remove, in order to make the sensors work. If we consider the example above, we only need to remove one furniture, which is the 3rd furniture from the left. After removing that, all sensors only go through at most 3 furnitures.

## Input

The first line contains three integers, 𝐿, 𝑛 and 𝑘, where 𝐿×𝐿 is the size of the apartment, 𝑛 is the number of furnitures, and 𝑘 is the largest number of furnitures that a sensor's signal can go through.

The next 𝑛 lines each contain four integers, 𝑎, 𝑏, 𝑐, 𝑑, specifying a furniture taking space (𝑎,𝑏) to (𝑐,𝑑). For all such lines, 𝑏=𝑑.

There can be multiple furnitures share the same column id. But for any two furnitures, they won't overlap.

## Output

The output only contains one integer, which is the smallest number of furnitures that need to be removed from the apartment.

## Examples

### input
```

9 7 3
6 1 9 1
1 2 3 2
3 4 7 4
3 5 5 5
2 7 4 7
7 6 9 6
6 8 8 8

```

### output
```

1

```

### input
```

20 8 4
9 6 17 6
2 7 17 7
5 8 8 8
1 1 4 1
2 5 9 5
8 4 10 4
6 2 10 2
5 3 17 3

```

### output
```

2

```

## Note

For 20% of the test cases, 𝑛, 𝑘, 𝐿 ≤ 10.

For 50% of the test cases, 𝑛, 𝑘, 𝐿 ≤ 100.

For 100% of the test cases, 𝑛, 𝑘, 𝐿 ≤ 10⁵.

Howard's security system had caught two people in total. The first one was Penny. She was entering the room right after the scene mentioned at the beginning of the problem, and was caught by a net from the ceiling. Sheldon complained that the net is a "wonderful security system if we're attacked by a school of tuna". Howard responded that "Don't worry, the net's going to be electrified." Sheldon was happy about this.

Then the second person caught by the net was Sheldon himself, when he was too panic at night and went out of the room to the bathroom. Unfortunately, the net had been electrified at that time, and worked just as he expected.

