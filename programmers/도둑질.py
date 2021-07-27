# https://programmers.co.kr/learn/courses/30/lessons/42897?language=python3

def solution(money):
    dp = [money[0], money[0]]
    dp2 = [0, money[1]]
    length = len(money)
    
    if len(money) == 3:
        return max(money)
    
    
    for i in range(2, length-1):
        dp.append(max(dp[-1], dp[-2]+money[i]))
    
    for j in range(2, length):
        dp2.append(max(dp2[-1], dp2[-2]+money[j]))
    
    return max(dp[-1], dp2[-1])
