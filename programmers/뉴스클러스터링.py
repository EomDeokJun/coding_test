# https://programmers.co.kr/learn/courses/30/lessons/17677?language=python3

from collections import OrderedDict
from string import ascii_lowercase

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    
    str1_dict = OrderedDict()
    str2_dict = OrderedDict()
    
    for idx in range(len(str1)-1):
        temp = str1[idx:idx+2]
        if temp[0] in ascii_lowercase:
            if temp[1] in ascii_lowercase:
                if temp not in str1_dict:
                    str1_dict[temp] = 1
                else:
                    str1_dict[temp] += 1

    for idx in range(len(str2)-1):
        temp = str2[idx:idx+2]
        if temp[0] in ascii_lowercase:
            if temp[1] in ascii_lowercase:
                if temp not in str2_dict:
                    str2_dict[temp] = 1
                else:
                    str2_dict[temp] += 1                    
    
    check_set = set(str1_dict.keys()).union(set(str2_dict.keys()))
    a = 0
    b = 0
    
    
    if len(check_set) == 0:
        return 65536
    else:
        for key in check_set:
            if key in str1_dict:
                if key in str2_dict:
                    a += min(str1_dict[key], str2_dict[key])
                    b += max(str1_dict[key], str2_dict[key])
                else:
                    b += str1_dict[key]
            else:
                if key in str2_dict:
                    b += str2_dict[key]
                    
                
                
    answer = int(a/b*65536)
    return answer
