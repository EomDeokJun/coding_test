# https://programmers.co.kr/learn/courses/30/lessons/12978


from collections import defaultdict

def solution(N, road, K):
    graph = [[0]*N for _ in range(N)]
    neighbors = defaultdict(list)
    answer = 0
    for r in road:
        if graph[r[0]-1][r[1]-1] != 0:
            graph[r[0]-1][r[1]-1] = min(graph[r[0]-1][r[1]-1] , r[2])
            graph[r[1]-1][r[0]-1] = min(graph[r[1]-1][r[0]-1], r[2])        
        else:
            
            graph[r[0]-1][r[1]-1] = r[2]
            graph[r[1]-1][r[0]-1] = r[2]
            neighbors[r[0]-1].append(r[1]-1)
            neighbors[r[1]-1].append(r[0]-1)
        
    cur = 0
    dists = defaultdict(lambda:float('inf'), {})
    dists[0] = 0
    
    unvisited = {k:float('inf') for k in range(N)}
    del unvisited[0]
    
    while unvisited:
        
        for node in neighbors[cur]:
            if node in unvisited:
                min_dist = min(dists[node], dists[cur]+graph[cur][node])
                dists[node] = min_dist
                unvisited[node] = min_dist
        
        min_node = min(list(unvisited.keys()), key=lambda x: unvisited[x])
        
        cur = min_node
        del unvisited[min_node]

        
    for i in range( N):
        if dists[i] <= K:
            answer += 1
    
    return answer
