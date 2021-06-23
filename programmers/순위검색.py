# https://programmers.co.kr/learn/courses/30/lessons/72412?language=python3


from collections import defaultdict
from itertools import product
import bisect

def gen_keys(info):
    return list(product(*[(info[0],"-"), (info[1],"-"), (info[2],"-"), (info[3], "-")]))
    
def solution(info, query):
    answer = []
    cat_dict = defaultdict(list)
    
    for i in info:
        i = i.split(" ")
        temp_keys = gen_keys(i)
        
        for key in temp_keys:
            cat_dict[key].append(int(i[4]))
            
    for key in cat_dict.keys():
        cat_dict[key] = sorted(cat_dict[key])
    
    for q in query:
        q = q.split(" and ")
        q = q[:-1] + q[-1].split(" ")
        q[4] = int(q[4])
        key = tuple(q[:-1])
        answer.append(len(cat_dict[key])-bisect.bisect_left(cat_dict[key], q[4]))

    return answer
