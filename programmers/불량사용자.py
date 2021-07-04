# https://programmers.co.kr/learn/courses/30/lessons/64064?language=python3


from collections import defaultdict
from itertools import product, combinations

def solution(user_id, banned_id):
    
    answer = 0
    falses = defaultdict(list)
    ban_count = defaultdict(int)
    
    for ban in banned_id:
        ban_count[ban] += 1
        
        if ban not in falses:
            start_idx = [idx for idx, b in enumerate(ban) if b == "*"]            
            for user_idx, user in enumerate(user_id):

                if len(ban) == len(user):
                    same = True
                    for b, u in zip(*[ban, user]):
                        if b != "*":
                            if b != u:
                                same = False
                                break
                    if same:
                        falses[ban].append(user_idx)  
    
    for k, v in ban_count.items():
        falses[k] = list(combinations(falses[k], v))
    
    
    
    temp_all_cases = set(product(*list(falses.values())))

    
    all_cases = list()
    length = len(banned_id)
    
    for case in temp_all_cases:
        case = set(sum(case, ()))

        if case not in all_cases:
            if len(case) == length:
                all_cases.append(case)
                
    answer = len(all_cases)

    return answer                        
