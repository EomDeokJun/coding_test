# https://programmers.co.kr/learn/courses/30/lessons/81303


def solution(n, k, cmd):

    removed = list()
    answer = ["O"]*n
    
    linked_list = [[None, 1]] + [[i-1, i+1]  for i in range(1, n-1)] + [[n-2, None]]
    
    for c in cmd:
        if c == "C":
            up = linked_list[k][0]
            down = linked_list[k][1]
            
            if up is not None:
                linked_list[up][1] = down  
            if down is not None:
                linked_list[down][0] = up
                
            removed.append((k, up, down))   
            linked_list[k] = [None, None]
            if down is None:
                k = up
            else:
                k = down
        
        elif c == "Z":
            num, up, down = removed.pop(-1)
            linked_list[num] = [up, down]
            if up is not None:
                linked_list[up][1] = num
            if down is not None:
                linked_list[down][0] = num
                           
        else:
            direction, dist = c.split()
            moved = 0
            dist = int(dist)      
            if direction == "D":
                while moved < dist:
                    k = linked_list[k][1]    
                    moved += 1     
            else:
                while moved < dist:
                    k = linked_list[k][0]    
                    moved += 1    

    for r in removed:
        answer[r[0]] = "X"
    return "".join(answer)
