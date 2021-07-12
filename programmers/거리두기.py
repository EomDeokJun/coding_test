# https://programmers.co.kr/learn/courses/30/lessons/81302?language=python3

from itertools import product
from collections import defaultdict

def gen_graph(p):
    node = list(product([0,1,2,3,4],[0,1,2,3,4]))
    graph = defaultdict(list)
    
    for n in node:
        if n[0]+1 <=4:
            if p[n[0]+1][n[1]] != 'X':
                graph[(n, p[n[0]][n[1]])].append(((n[0]+1, n[1]), p[n[0]+1][n[1]]))

        if n[1]+1 <=4:
            if p[n[0]][n[1]+1] != 'X':
                graph[(n, p[n[0]][n[1]])].append(((n[0], n[1]+1), p[n[0]][n[1]+1]))     

        if n[0]-1 >=0:
            if p[n[0]-1][n[1]] != 'X':
                graph[(n, p[n[0]][n[1]])].append(((n[0]-1, n[1]), p[n[0]-1][n[1]]))  
        if n[1]-1 >=0:
            if p[n[0]][n[1]-1] != 'X':
                graph[(n, p[n[0]][n[1]])].append(((n[0], n[1]-1), p[n[0]][n[1]-1]))
    
    return node, graph

def dfs(visits, current, graph, ans):
    visits.append(current)
    
    
#     if ans == 0:
#         del visits[-1]
#         return ans
    
    if len(visits) >= 2:
        if current[1] == 'P':
            del visits[-1]
            return 0
    if len(visits) == 3:
        del visits[-1]
        return 1
    
    
    for neighbor in graph[current]:
        if neighbor not in visits:
            ans = dfs(visits, neighbor, graph, ans)
            if ans == 0:
                break
    
    
    del visits[-1]
    
    return ans
    

def solution(places):
    answer = []
    
    for p in places:
        node, graph = gen_graph(p)
        wrong = False
        for n in node:
            n = (n, p[n[0]][n[1]])
            if n[1] == 'P':
                ans = dfs([], n, graph, 1)
                if ans == 0:
                    wrong = True
                    answer.append(0)
                    break
        if not wrong:
            answer.append(1)

    return answer
