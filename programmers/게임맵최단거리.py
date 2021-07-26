# https://programmers.co.kr/learn/courses/30/lessons/1844?language=python3

from collections import deque
from collections import defaultdict

def solution(maps):
    parents = dict()
    dists = defaultdict(lambda:float('inf'), {})
    visited = defaultdict(int)
    
    N = len(maps)
    M = len(maps[0])    
    
    q = deque([])

    cur = (0,0)
    
    q.append(cur)
    dists[cur] = 1
    
    while True:
        if not q:
            break
        
        cur = q.popleft()
        
        nexts =  [(cur[0]-1, cur[1]), (cur[0], cur[1]-1), 
                    (cur[0]+1, cur[1]), (cur[0], cur[1]+1)]
    
        for n in nexts:
            if n[0]>=0 and n[0]<N and n[1]>=0 and n[1]<M:
                if visited[n] == 0 and maps[n[0]][n[1]] == 1:
                    visited[n] = 1
                    new_dist = dists[cur] + 1
                    if dists[n]>=new_dist:
                        q.append(n)
                        dists[n] = new_dist
                        parents[n] = cur
                    if n == (N-1, M-1):
                        return dists[n]
    
        visited[cur] = 1
    
    if dists[(N-1, M-1)] == float('inf'):
        return -1
    else:
        return dists[(N-1, M-1)]
