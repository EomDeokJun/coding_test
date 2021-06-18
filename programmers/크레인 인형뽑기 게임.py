# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    bowl = list()
    for move in moves:
        for b in board:
            if b[move-1] != 0:
                if len(bowl) == 0:
                    bowl.append(b[move-1])
                else:
                    if bowl[-1] == b[move-1]:
                        del bowl[-1]
                        answer += 2
                    else:
                        bowl.append(b[move-1])
                 
                b[move-1] = 0
                # print(bowl)
                break
    return answer
