# https://programmers.co.kr/learn/courses/30/lessons/49190?language=python3

from collections import defaultdict

def get_loc(cur, a):
    if a == 0:
        return (cur[0], cur[1]+1)
    elif a == 1:
        return (cur[0]+1, cur[1]+1)
    elif a == 2:
        return (cur[0]+1, cur[1])
    elif a == 3:
        return (cur[0]+1, cur[1]-1)
    elif a == 4:
        return (cur[0], cur[1]-1)
    elif a == 5:
        return (cur[0]-1, cur[1]-1)
    elif a == 6:
        return (cur[0]-1, cur[1])
    elif a == 7:
        return (cur[0]-1, cur[1]+1)

def get_graph(arrows):
    graph = defaultdict(list)
    
    cur = (0,0)
    
    for a in arrows:
        for _ in range(2):
            new_cur = get_loc(cur, a)
            graph[cur].append(new_cur)
            graph[new_cur].append(cur)
            cur = new_cur
    
    return graph

def solution(arrows):
    answer = 0
    graph = get_graph(arrows)
    v = 0
    e = 0
    for node, neighbors in graph.items():
        v += 1
        e += len(set(neighbors))
    
    answer = 1 - v + e//2
    
    
    return answer
