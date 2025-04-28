import bisect

"""
The plan of attack is to determine how many train cars are destroyed by each attack.
Each train car is placed at a position with a defense value. 
So attack has:
1. A center position (y),
2. A radius (b), which defines its range [y - b, y + b],
3. An attack power (A).

A train car can be destroyed by an attack if:
1. If it's in the range of the attack area, and
2. It's defense value is ≤ attack power.

For efficiency that is to cover 10^5 train cars and 10^5 attacks, we can try to:
1. Should first sort all train cars by the given position.
2. Build a segment tree that carries the minimum defense value in any interval, then, 
3. For each attack that takes place:
   a. Use Binary search for finding the index of the range of caris in the attack zone
   b. Use the segment tree to repeatedly find and remove cars with defense ≤ A.

So once a car is destroyed by any attack, it is removed from consideration in future attacks.

Time Complexity:
1. Sorting the train cars: O(n log n)
2. Segment tree construction: O(n)
3. Each attack:
   a. Binary search to find range: O(log n)
   b. While loop per car destroyed: O(log n) per removal
   → So total destruction processing over all attacks: O(n log n)
Thus, total time complexity: O((n + m) log n)

References:
1. https://www.youtube.com/watch?v=ciHThtTVNto
2. https://www.geeksforgeeks.org/segment-tree-range-minimum-query/
3. https://cp-algorithms.com/data_structures/segment_tree.html
"""
 
INF = 10 ** 18 # marks a wagon that has been demolish
 
 
 
def build_segment_tree(values):
    
    n = len(values)
    size = 1
    while size < n:
        size *= 2
 
    
    tree = [(INF, -1)] * (2 * size) # tree has 2 x size nodes, leaves start at size
 
    for i, v in enumerate(values):
        tree[size + i] = (v, i)
 
    
    for i in range(size - 1, 0, -1):
        left, right = tree[2 * i], tree[2 * i + 1]
        tree[i] = left if left[0] <= right[0] else right
    return tree, size
 
 
def point_update(tree, leaf_offset, idx, new_val):
    
    i = leaf_offset + idx
    tree[i] = (new_val, idx)
    i //= 2
    while i:
        left, right = tree[2 * i], tree[2 * i + 1]
        tree[i] = left if left[0] <= right[0] else right
        i //= 2
 
 
def range_min(tree, leaf_offset, l, r):
 
    # l, r -> left, right child
    l += leaf_offset
    r += leaf_offset
    
    best = (INF, -1)
 
    while l <= r:
        if l % 2 == 1:
            if tree[l][0] < best[0]:
                best = tree[l]
            l += 1
        
        
        if r % 2 == 0: 
            if tree[r][0] < best[0]:
                best = tree[r]
            r -= 1
        
        l //= 2
        r //= 2
    
    
    return best
 
 
n = int(input())
wagons = [tuple(map(int, input().split())) for _ in range(n)]
wagons.sort()                                 
 
pos     = [x for x, _ in wagons]
defence = [d for _, d in wagons]
 
tree, offset = build_segment_tree(defence)
 
m = int(input())
for _ in range(m):
    a, b, y = map(int, input().split())
 
    left, right = y - b, y + b
    
    l_idx = bisect.bisect_left(pos, left)
    r_idx = bisect.bisect_right(pos, right) - 1
 
    # no wagons in range
    if l_idx > r_idx:          
        print(0)
        continue
 
    demolish = 0
    
    while True:
        mn, idx = range_min(tree, offset, l_idx, r_idx)
        
        # all remaining wagons are stronger
        if mn > a:             
            break
        
        point_update(tree, offset, idx, INF)
        demolish += 1
 
    print(demolish)