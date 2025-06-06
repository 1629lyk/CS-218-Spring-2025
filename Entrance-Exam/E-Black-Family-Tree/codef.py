"""
find largest connected group of loyal family members in the harry potter family tree
references:
https://courses.washington.edu/css343/zander/NotesProbs/graphBFS.pdf

https://youtu.be/7gv3aEHcs2U?si=ndiDtb588MYBBWr3
"""

import sys
from collections import deque 
input = sys.stdin.readline 


def graph_creat(n, parent_inputs):
    graph = [[] for _ in range(n)]
    
    for f_child in range(1, n): # build undirected family graph pointing both directions p->c and c->p for 2 way traveseral 
        f_parent = parent_inputs[f_child - 1]
        graph[f_parent].append(f_child)
        graph[f_child].append(f_parent)
    
    return graph

def bfs_c_size(graph, start, visited, traitors):
    if traitors[start]:  
        return 0
    
    queue = deque([start]) 
    loy_size = 0
    
    while queue:
        node = queue.popleft() 
        
        if visited[node] or traitors[node]: 
            continue
        
        visited[node] = True 
        loy_size += 1
        
        for neighbor in graph[node]:
            if not visited[neighbor] and not traitors[neighbor]:
                queue.append(neighbor) 
    
    return loy_size 
 
def find_larg_comp(n, graph, traitors):
    visited = [False] * n # more efficient for around 10^6 data than python set()
    loy_max_size = 0
    
    for node in range(n):
        if not visited[node] and not traitors[node]:
            loy_size = bfs_c_size(graph, node, visited, traitors)
            loy_max_size = max(loy_max_size, loy_size) 
    
    return loy_max_size
 
def main():
    n, m = map(int, input().split())
    parent_inputs = [int(input()) for _ in range(n - 1)]
    traitors = [False] * n
    
    for _ in range(m):
        traitors[int(input())] = True
 
    graph = graph_creat(n, parent_inputs)
    print(find_larg_comp(n, graph, traitors))
 
if __name__ == "__main__":
    main()