# https://programmers.co.kr/learn/courses/30/lessons/42842?language=python3


def solution(brown, yellow):
    answer = []
    
    for i in range(1, int(yellow**(1/2))+1):
        
        if yellow % i == 0:
            j = yellow / i
            
            if (j + 2)*(i+2) - yellow == brown:
                
                return [j+2, i+2]
        
