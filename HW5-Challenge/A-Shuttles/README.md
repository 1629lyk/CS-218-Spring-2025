# A. Shuttles

**Time Limit:** 1 second  
**Memory Limit:** 256 megabytes

---

This problem is from UCRPC, themed in 2024 Summer Olympic Games.

During the Olympic Games, most spectators are expected to travel by subway to various venues. To facilitate this, the event organizers plan to operate shuttle services between each venue and all nearby subway stations within a distance of 𝑑.

These shuttles are environmentally friendly electric vehicles, necessitating the strategic placement of charging stations. Therefore, we must ensure that each shuttle route between a venue and a subway station has at least one charging station at either endpoint (venue or subway station). This will allow the shuttles to recharge as needed while minimizing infrastructure costs.

Given the coordinates of all subway stations and event venues, your task is to minimize the number of charging stations for all shuttles.

---

## Input

The first line contains three integers `n`, `m`, `d`. This means that there are:

- `n` subway stations  
- `m` venues  
- `d` is the maximum Euclidean distance within which a shuttle will be established from a venue to a station

The next `n` lines each contain two integers `x` and `y`, which is the coordinate of subway station `i`.

The next `m` lines each contain two integers `x` and `y`, which is the coordinate of venue `i`.

---

## Output

The output only contains one integer, which is the **minimum number of charging stations** to guarantee that each shuttle can access a charging station on at least one endpoint of its route.

---

## Example

### Input
```
1 2 1
1 1
2 1
1 2
```

### Output
```
1
```

---

## Note

- In 30% of the test data, `n, m ≤ 10`
- In 100% of the test data, `n, m ≤ 10^3`, and all coordinates and `d` are **positive integers** within `1000`

---

## Fun Fact

Recent Olympic Games have seen a push towards more sustainable transport options.  
In the 2016 Rio de Janeiro Olympics, **electric buses** were introduced to reduce carbon emissions.
