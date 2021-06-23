# https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3

from itertools import combinations
from collections import defaultdict


def dfs(begin, target, counts, visits, adj):
    visits[begin] = True
    counts += 1
    # print(begin, counts)
    if begin == target:
        visits[begin] = False
        return counts, visits
    if set(visits.values()) == {True}:
        visits[begin] = False
        return 51, visits
    

    
    temp_counts = list()
    for w in adj[begin]:
        if visits[w] == False:
            c, visits = dfs(w, target, counts, visits, adj)
            temp_counts.append(c)
    # print(temp_counts)       
    if len(temp_counts) == 0:
        counts = 51
    else:
        counts = min(temp_counts)
    visits[begin] = False
    
    # print(visits)
    return counts, visits
    
def check_adj(w1, w2):
    dif = 0
    for l1, l2 in zip(w1, w2):
        if l1!=l2:
            dif += 1
        if dif > 1:
            return 0
    return 1
    
    
    
def solution(begin, target, words):
    answer = -1
    words.append(begin)
    visits = {w:False for w in words}
    
    words_adj = defaultdict(list)
    
    comb = combinations(list(range(len(words))), 2)
    
    for idx1, idx2 in comb:
        adj = check_adj(words[idx1], words[idx2])
        
        if adj == 1:
            words_adj[words[idx1]].append(words[idx2])
            words_adj[words[idx2]].append(words[idx1])
    # print(words_adj)
    
    answer, visits = dfs(begin, target, answer, visits, words_adj)
    
    if answer == 51:
        answer = 0
    
    
    return answer
