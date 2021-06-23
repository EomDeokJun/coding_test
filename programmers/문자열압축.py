#https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3

def solution(s):
    answer = 0
    length = len(s)
    all_answer = list()
    answer = [1]
    
    for i in range(1, int(length/2)+2):
        cur = 0
        temp_answer = ""
        count = 1
        cur_string = ""
        
        while cur < length:
            if cur_string == "":
                if s[cur:cur+i] == s[cur+i:cur+2*i]:
                    cur_string = s[cur:cur+i]
                    cur += i
                    count += 1
                    
                else:
                    temp_answer += s[cur:cur+i]
                    count = 1
                    cur += i
                    cur_string = ""
            else:
                if s[cur+i:cur+2*i] == cur_string:
                    cur += i
                       
                    if cur == length:
                        temp_answer += f"{count}{cur_string}"
                    
                    count += 1    
                else:
                    if count > 1:
                        temp_answer += f"{count}{cur_string}"
                        count = 1
                        cur += i
                        cur_string = "" 
                    else:
                        cur_string += s[cur:cur+i] 
                        count = 1
                        cur += i
                        
        all_answer.append((temp_answer, len(temp_answer)))
    # print(all_answer)
    answer = sorted(all_answer, key=lambda x: x[1])[0][1]
        
    return answer
