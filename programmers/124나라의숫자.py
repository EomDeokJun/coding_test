# https://programmers.co.kr/learn/courses/30/lessons/12899?language=python3

def solution(n):
    answer = list()
    m = 1
    
    while n > 0:
        res = n % 3**m
        if res >= 1 and res <= 3**m//3:
            answer = ['1'] + answer
        elif res >= 3**m//3 + 1 and res <= 3**m//3*2:
            answer = ['2'] + answer
        else:
            answer = ['4'] + answer

        n -= 3**m
        m += 1
        
    answer = "".join(answer)
    return answer
