# https://programmers.co.kr/learn/courses/30/lessons/60058?language=python3

from collections import Counter
from collections import  deque

def check_correct(p):
    q = deque()
    length = len(p)
    idx = 0
    while idx < length:
        if len(q) == 0:
            q.append(p[idx])
            idx += 1
        elif q[-1] == "(" and p[idx] == ")":
            q.pop()
            idx += 1
        else:
            q.append(p[idx])
            idx += 1
    
    if len(q) == 0:
        return True
    else:
        return False


def solution(p):
    if p == "":
        return ""
    
    if check_correct(p):
        return p
    
    else:
        for i in range(2, len(p)+1, 2):
            counts = list(Counter(p[:i]).values())
            if len(counts) == 2:
                if counts[0] == counts[1]:
                    u = p[:i]
                    v = p[i:]
                    break
        if check_correct(u):
            return u + solution(v)
        else:
            result = "("
            result += solution(v)
            result += ")"
            for one_u in u[1:-1]:
                if one_u == "(":
                    result += ")"
                else:
                    result += "("
            return result
