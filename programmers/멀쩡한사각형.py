# https://programmers.co.kr/learn/courses/30/lessons/62048?language=python3

import math

def gcd(x, y):
    while y:
        x, y = y, x % y
        
    return x

def solution(w,h):
    answer = 0
    
    a = gcd(w,h)
    w_small = int(w/a)
    h_small = int(h/a)
    
    if w_small < h_small:
        for k in range(1, w_small):
            answer += h_small - math.ceil(k*h_small/w_small)
            
    else:
        for k in range(1, h_small):
            answer += w_small - math.ceil(k*w_small/h_small)

    not_in = (w_small*h_small - answer*2)*a

    answer = w*h-not_in
    
    return answer
