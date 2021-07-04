# https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3

from collections import defaultdict


def solution(N, stages):
    answer = []
    answer_count = defaultdict(int)
    
    for s in stages:
        answer_count[s] += 1
    
    fault_rate = defaultdict(int)
    
    for n in range(1, N+1):
        a = answer_count[n]
        b = 0
        for i in range(n, N+2):
            b += answer_count[i]
        
        if b != 0:
            fault_rate[n] = a/b

    answer = sorted(list(range(1, N+1)), key=lambda x: (-fault_rate[x], x))    
    
    return answer
    
