# F. Journalist

**Time Limit per Test:** 1 second  
**Memory Limit per Test:** 256 megabytes

This problem is from UCRPC, themed in the 2024 Summer Olympic Games.

---

Imagine you are a journalist for a news agency in Paris. Your task is to report events happening at various venues across the city. You have a map of Paris, which can be viewed as a graph with \(n\) vertices as major places and crossroads, and \(m\) edges as roads connecting them. Among the \(n\) vertices, \(p\) of them are venues where the events happen. Each day, you will be stationed at one of these venues, but in case a major event happens at any venue, you need to quickly cycle there to cover the news.

Given the lengths of the roads in meters, you want to know the minimum cycling speed required in meters per second to ensure that you can travel from any venue to any other venue within \(t\) minutes, no matter where the news breaks.

---

## Input

- The first line contains two integers \(n\) and \(m\), indicating the number of vertices and edges on the map, respectively. The vertices are labeled from \(0\) to \(n-1\).
- The second line contains an integer \(p\), which is the number of venues.
- The third line contains \(p\) integers, which are the vertex labels of the venues.
- The fourth line contains an integer \(t\) specifying the maximum allowed travel time in minutes to reach any venue in case of a major event.
- The next \(m\) lines describe \(m\) edges. Each line contains three integers \((u,v,l)\) where \(u\) and \(v\) are the vertices connected by an edge, and \(l\) is the length of the edge in meters. 

It is guaranteed that you can move from any vertex to any other vertex along these edges.

---

## Output

- The output contains a single float with three digits after the decimal point, which is the minimum cycling speed required in meters per second.

---

## Example

**Input**
```
4 3
3
1 2 3
1
0 1 5
0 2 8
0 3 10
```

**Output**
```
0.300
```

---

## Note

All input values are positive integers.

- For 30% of the test data: \(p = 2\), \(n \leq 100\), \(m \leq 100\).
- For 50% of the test data: \(2 \leq p \leq 10\), \(n \leq 1000\), \(m \leq 10000\).
- For 100% of the test data: \(2 \leq p \leq 100\), \(n \leq 10000\), \(m \leq 100000\).
- The road length \(l \leq 100\).

---

## Fun Facts

There is a long history of bringing news about the Olympic Games all over the world:

- The 1936 Berlin Olympics were the first to be televised, marking a significant milestone in sports broadcasting. The coverage was limited to local audiences in Berlin and surrounding areas.
- In 1964, the Tokyo Olympics were the first to be broadcast internationally via satellite, making it possible for audiences around the world to watch the events live.
- In 2008, the Beijing Olympics was the first Olympics where live events could be watched online extensively.
- The 2016 Rio de Janeiro Olympics featured virtual reality broadcasting for the first time.
