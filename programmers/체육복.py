# https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3

def solution(n, lost, reserve):
    answer = n - len(lost)

    remove_id = list()
    
    for id in lost:
        if id in reserve:
            answer +=1 
            del reserve[reserve.index(id)]
            remove_id.append(id)
            
    for id in remove_id:
        del lost[lost.index(id)]
    
    for id in lost:
        if id-1 in reserve:
            del reserve[reserve.index(id-1)]
            answer += 1
        elif id+1 in reserve:
            del reserve[reserve.index(id+1)]
            answer += 1
    
    return answer
