# https://programmers.co.kr/learn/courses/30/lessons/42890?language=python3

from itertools import combinations

def solution(relation):
    answer = 0
    keys = list()
    ncol = len(relation[0])
    nrow = len(relation)
    
    col_list = list(range(ncol))
    
    for n in range(1, ncol+1):
        comb = list(combinations(col_list, n))
        
        for com in comb:
            is_subset = False
            
            for k in keys:
                if k.issubset(set(com)):
                    is_subset = True
                    break
                    
            if is_subset is False:
                temp_rel = ["".join([elem[c] for c in com]) for elem in relation]  

                if len(set(temp_rel)) == nrow:
                    answer += 1
                    keys.append(set(com))
                    
    return answer
