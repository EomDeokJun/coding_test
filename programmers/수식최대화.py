#https://programmers.co.kr/learn/courses/30/lessons/67257?language=python3#

import re
from itertools import permutations
import math

def solution(expression):
    original_ops = re.split("[0-9]+", expression)[1:-1]
    original_numbers = re.split("[\*\-\+]+", expression)
    original_numbers = [int(i) for i in original_numbers]
    op_list = set(original_ops)
    op_orders = list(permutations(op_list))

    answer = list()
    for op_order in op_orders:
        numbers = original_numbers.copy()

        temp_ops = original_ops.copy()
        for one_op in op_order:
            used = 0
            
            temp_temp_ops = list()

            for op_idx, op in enumerate(temp_ops):
                if op == one_op:
                    if op == "*":
                        numbers = numbers[:op_idx+used] + [numbers[op_idx+used]*numbers[op_idx+used+1]] + numbers[op_idx+used+2:]
                    if op == "+":
                        numbers = numbers[:op_idx+used] + [numbers[op_idx+used]+numbers[op_idx+used+1]] + numbers[op_idx+used+2:]
                    if op == "-":
                        numbers = numbers[:op_idx+used] + [numbers[op_idx+used]-numbers[op_idx+used+1]] + numbers[op_idx+used+2:]   
                    used -= 1
                else:
                    temp_temp_ops.append(op)

            temp_ops = temp_temp_ops.copy()
        answer.append(abs(numbers[0]))
    answer = max(answer)
    return answer
