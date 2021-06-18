# https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3

def solution(numbers, hand):
    answer = ''
    l_current = "*"
    r_current = "#"
    cord = {1:[1,4], 2:[2,4], 3:[3,4], 4:[1,3], 5:[2,3], 6:[3,3], 7:[1,2], 8:[2,2], 9:[3,2],
            "*":[1,1], "#":[3,1], 0:[2,1]}
    
    for num in numbers:
        
        if num in [1,4,7]:
            l_current = num
            answer += "L"   
        elif num in [3,6,9]:
            r_current = num
            answer += "R"
        else:
            l_dist = abs(cord[l_current][0]-cord[num][0]) + abs(cord[l_current][1]-cord[num][1])
            r_dist = abs(cord[r_current][0]-cord[num][0]) + abs(cord[r_current][1]-cord[num][1])

            if l_dist > r_dist:
                r_current = num
                answer += "R"
            elif l_dist < r_dist:
                l_current = num
                answer += "L"
            else:
                if hand == "right":
                    r_current = num
                    answer += "R"
                else:
                    l_current = num
                    answer += "L"                
    return answer
