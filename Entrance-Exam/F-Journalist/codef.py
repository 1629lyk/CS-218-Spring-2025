import heapq 

def dijkstra_algo(n, graph, start): 
    
    dis = [float('inf')] * n 
    dis[start] = 0 
    vis = [False] * n 
    heap = [(0, start)] 

    while heap:
        curr_dist, u = heapq.heappop(heap) 
        
        if vis[u]:
            continue 
        
        vis[u] = True

        for v, length in graph[u]:
            if dis[v] > curr_dist + length: # finds shorter path
                dis[v] = curr_dist + length 
                heapq.heappush(heap, (dis[v], v))
    
    return dis 

def compute_min_speed(n, m, p, venues, t, edges): 
    
    graph = [[] for _ in range(n)] 
    
    for u, v, l in edges:
        # 2 way insertion 
        graph[u].append((v, l))
        graph[v].append((u, l))

    max_venue_distance = 0  


    for venue in venues:
        sml_paths = dijkstra_algo(n, graph, venue)
        for other_venue in venues:
            if other_venue != venue:
                max_venue_distance = max(max_venue_distance, sml_paths[other_venue])

    t_secs = t * 60

    min_speed = max_venue_distance / t_secs

    # 3 decimal places as per question
    return (f"{min_speed:.3f}")

def main():
    
    
    n, m = map(int, input().split()) 
    p = int(input())
    
    venues = list(map(int, input().split()))
    t = int(input())
    edges = []
    
    for _ in range(m):
        u, v, l = map(int, input().split())
        edges.append((u, v, l))

    result = compute_min_speed(n, m, p, venues, t, edges)
    print(result)

if __name__ == "__main__":
    main()
