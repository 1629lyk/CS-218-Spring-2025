"""
Algorithm Explanation:

For a 5x5 grid, a player can start at any cell.
At each time unit, Chargin' Chucks will attack some tracks,
could be rows 1-5 or columns 6-10.

If a player is on a cell that lies on an attacked track, they are immediately eliminated.
Between each time unit, a player can move to an adjacent cell (up, down, left, right), 
or stay at the same cell.

The goal is to survive for as long as possible.

The plan of attack is to:
i. Start with all possible grid cells as alive at time 0.
ii. For each time unit:
    a. Move to all adjacent, or same cells.
    b. Remove all cells that are attacked during that time unit.
    c. If at any time no cells remain alive, the game ends at that time.
iii. If the player survives through all attacks, output the last attack time + 1.

Time Complexity:
1. Unit time take for each movement:
   a. Moving to adjacent cells: O(5x5 x 5) -> O(1), constant since grid size is fixed.
   b. Removing attacked cells: O(5) for each attack (at most 10 attacks per time unit).

2. Processing all attacks: O(n), 
where n is the number of Chargin' Chucks 
as each event is processed once.

Overall Time Complexity: O(n)

References:
1. https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/ 
"""


from collections import defaultdict

def initialize_grid():
    aliv = set()
    for r in range(5):
        for c in range(5):
            aliv.add((r, c))
    return aliv


def move_players(aliv):
    dirs = [(-1,0),(1,0),(0,-1),(0,1),(0,0)]
    next_alive = set()
    
    for r, c in aliv:
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < 5 and 0 <= nc < 5:
                next_alive.add((nr, nc))
    
    
    return next_alive

def map_attacks(attacks):
    attk_per_time = defaultdict(list)
    for t, x in attacks:
        attk_per_time[t].append(x)
    
    return attk_per_time



def get_attk_cells(tracks):
    attacked = set()
    for x in tracks:
        
        if 1 <= x <= 5:
            row = x - 1
            for c in range(5):
                attacked.add((row, c))
        
        
        else:
            col = x - 6
            for r in range(5):
                attacked.add((r, col))
    
    
    return attacked


def game_rules_sim(n, attacks):
    if n == 0:
        print(1)
        return

    attk_per_time = map_attacks(attacks)
    aliv = initialize_grid()
    curr_time = 0
    times = sorted(attk_per_time.keys())

    for t in times:
        
        while curr_time < t:
            aliv = move_players(aliv)
            if not aliv:
                print(curr_time)
                return
            curr_time += 1

        attk_cells = get_attk_cells(attk_per_time[t])
        
        
        aliv = aliv - attk_cells
        aliv = move_players(aliv)

        if not aliv:
            print(t)
            return

        curr_time = t + 1

    print(times[-1] + 1)

def main():
    n = int(input())
    attacks = []
    for _ in range(n):
        t, x = map(int, input().split())
        attacks.append((t, x))

    game_rules_sim(n, attacks)


if __name__ == "__main__":
    main()