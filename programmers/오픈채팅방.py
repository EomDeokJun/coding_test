# https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3

def solution(record):
    temp_answer = []
    id_name = dict()
    
    for rec in record:
        rec = rec.split()
        if rec[0] == 'Change':
            id_name[rec[1]] = rec[2]
        elif rec[0] == 'Enter':
            temp_answer.append([rec[1], '님이 들어왔습니다.'])
            id_name[rec[1]] = rec[2]
        else:
            temp_answer.append([rec[1], '님이 나갔습니다.'])

    answer = list()
    
    for temp in temp_answer:
        answer.append(f"{id_name[temp[0]]}{temp[1]}")
    
    
    
    return answer
