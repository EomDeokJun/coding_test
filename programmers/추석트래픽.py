# https://programmers.co.kr/learn/courses/30/lessons/17676?language=python3


from collections import deque

def solution(lines):
    answer = 0
    time_lines = list()

    for l in lines:
        l = l.split()[1:]
        end = l[0].split(":")
        end = int(end[0])*3600 + int(end[1])*60 + int(float(end[2])*1000)/1000
        start = end - int(float(l[1][:-1])*1000)/1000 + 0.001
        time_lines += [(start, 0), (end, 1)]
        
    time_lines = sorted(time_lines)
    q = deque()
    q_len = 0
    max_len = 0
    total_time = len(time_lines)

    idx = 0
    while idx < total_time:
        if len(q) == 0:
            q.append(time_lines[idx])
            if time_lines[idx][1] == 0:
                q_len += 1
                if q_len > max_len:
                    max_len = q_len
            idx += 1

        else:
            if time_lines[idx][0]-q[0][0] < 1:
                q.append(time_lines[idx])
                
                if time_lines[idx][1] == 0:
                    q_len += 1
                    if q_len > max_len:
                        max_len = q_len
                idx += 1
            else:
                t = q.popleft()
                if t[1] == 1:
                    q_len -=1
            
    answer = max_len
    return answer
