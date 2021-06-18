# https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3

import string


def solution(new_id):
    new_id = new_id.lower()
    case = list(string.ascii_lowercase) + ['-','_','.'] + ['1','2','3','4','5','6','7','8','9','0']
    
    temp_new_id = new_id
    new_id = ""

    for idx, i in enumerate(temp_new_id):
        if i in case or type(i) == int:
            if len(new_id) > 0:
                if not (i == '.' and new_id[-1]=='.'):

                    new_id += i
            else:
                if  i != '.':
                    new_id += i

    if len(new_id)>0 and new_id[-1] == '.':
        new_id = new_id[:-1]
    if len(new_id) == 0:
        new_id = 'a'
    if len(new_id)>=16:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]   
        
    if len(new_id)<=2:
        new_id += new_id[-1]*(3-len(new_id))
    
    
    return new_id
