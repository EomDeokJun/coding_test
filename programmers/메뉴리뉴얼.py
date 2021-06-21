# https://programmers.co.kr/learn/courses/30/lessons/72411?language=python3#


from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer= dict()

    course = sorted(course, reverse=True)
    orders = [sorted(o) for o in orders]
    for i in course:
        count = Counter()
        for o in orders:
            count.update(list(combinations(o,i)))

        
        if len(count) >0:
            
            count = sorted(count.items(), key=lambda x: x[1], reverse=True)
            count = {k:v for k, v in count}
            max_count = list(count.values())[0]

            for k, v in count.items():
                if v<=1:
                    break
                else:
                    if v == max_count:
                        answer["".join(k)] = v
                    else:
                        break

    answer = sorted(list(answer.keys()))

    return answer
