"""
Understanding the Problem:

Play piano piece by pressing a sequence of keys 
using two hands in a way that minimizes fatigue,
calculated the total distance a hand must move on a linear keyboard.

For each key press, one hand must be moved to that key. 
The fatigue increases by |x - y| when a hand moves from key x to key y.
The challenge is to decide which hand to use for each press to minimize total fatigue.

Plan of Attack:
- Dynamic programming with an offset trick.
- Let dp[l] be the minimum fatigue (excluding a shared offset) 
  when one hand is on the previously pressed key and the other is at position l.
- For each key press p, compute the cost of moving the other hand
  to p from all possible positions l, taking the best one.
- Use last used hand to the next key by increasing the global offset ofs by |p - prev|.
- The new best option is used to update dp[prev], 
  representing placing the other hand at prev and the active hand at p.

Finally, the answer is the minimum value in dp[1:] plus the total accumulated offset.

Time Complexity:
For each of the n presses, 
iterate through all k key positions to compute 
the best move: O(k)

Overall Time Complexity: O(n * k) per test case

References:
https://cp-algorithms.com/dynamic_programming/divide-and-conquer-dp.html 
"""


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))    
    

    # dp[l] = minimum fatigue minus the current global offset,
    # when one hand is at 'prev' and the other is at l.
    dp = [0] * (k + 1)

    ofs = 0
    prev = a[0]

    
    
    for p in a[1:]:
        q = prev
        
        b_ofs = ofs
        best = float('inf')
       
        # Scan all possible positions for the other hand
        for l in range(1, k + 1):
            cost = dp[l] + b_ofs + abs(p - l)
            
            
            if cost < best:
                best = cost

        # Check 1: move the 'q'-hand: add |p-q| to all states via offset
        ofs += abs(p - q)

        # Check 2: move the 'other hand': update the slot for l = q
        rel = best - ofs
        if rel < dp[q]:
            dp[q] = rel

        prev = p

    print(min(dp[1:]) + ofs)
