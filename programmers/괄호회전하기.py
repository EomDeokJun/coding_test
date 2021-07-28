# https://programmers.co.kr/learn/courses/30/lessons/76502?language=python3

from collections import deque

pairs = {"]":"[", ")":"(", "}":"{", "[":None, "(":None, "{":None}


def solution(s):
    answer = 0
    
    length = len(s)
    
    for start in range(length):
        q = deque()
        cur = start
        q.append(s[cur])
        if cur == length -1:
            cur = 0
        else:
            cur += 1

        while cur != start:
            cur_string = s[cur]
            if len(q) == 0:
                q.append(cur_string)
            elif q[-1] == pairs[cur_string]:
                q.pop()
            else:
                q.append(cur_string)
            
            if cur == length-1:
                cur = 0
            else:
                cur += 1
        if len(q) == 0:
            answer += 1
    
    return answer
