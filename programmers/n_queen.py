# https://programmers.co.kr/learn/courses/30/lessons/12952?language=python3


def check_valid(i, k, cols):
    
    for j in range(0, i):
        if cols[j] == k:
            return False
        
        if cols[j] + j == k + i:
            return False
        if cols[j] - j == k - i:
            return False

    
    return True
    
def dfs(i, cols, n, answer):

    if i == n-1:
        for k in range(0, n):
            
            if check_valid(i, k, cols):
                answer += 1

        
    else:
        for k in range(0, n):

            if check_valid(i, k, cols):
                cols[i] = k
                answer = dfs(i+1, cols, n, answer)
    return answer

def solution(n):
    answer = 0
    
    cols = [-1]*n
    answer = dfs(0, cols, n, answer)
    
    return answer
