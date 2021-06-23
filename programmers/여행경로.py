# https://programmers.co.kr/learn/courses/30/lessons/43164?language=python3#

from collections import defaultdict
from itertools import combinations

def get_adj(tickets):
    
    ticket_table = defaultdict(list)
    tickets = list(combinations(tickets, 2))
    used = list()
    for t1, t2 in tickets:
        if (t1, t2) not in used:
            if t1[0][1] == t2[0][0]:
                ticket_table[t1].append(t2)
            if t2[0][1] == t1[0][0]:
                ticket_table[t2].append(t1)
            used.append((t1, t2))
            
    for k in ticket_table:
        ticket_table[k] = sorted(list(set(ticket_table[k])))
    return ticket_table        


def dfs(ticket, used_tickets, ticket_table, total_tic):
    used_tickets.append(ticket)
    
    if len(used_tickets) == total_tic:
        return used_tickets

    for t in ticket_table[ticket]:
        if t not in used_tickets:
            used_tickets = dfs(t, used_tickets, ticket_table, total_tic)
            if len(used_tickets) == total_tic:
                return used_tickets
            
    del used_tickets[used_tickets.index(ticket)]
    # del used_tickets[-1]
    
    return used_tickets
    
    

def solution(tickets):
    tickets = sorted([tuple(t) for t in tickets])
    tickets = [(t, idx) for idx, t in enumerate(tickets)]
    ticket_table = get_adj(tickets)
    
    total_tic = len(tickets)
    
    for t in tickets:
        if t[0][0] == "ICN":
            used_tickets = list()
            used_tickets = dfs(t, used_tickets, ticket_table, total_tic)

            if len(used_tickets) == total_tic:
                break
    
    answer = [t[0][0] for t in used_tickets]
    answer.append(used_tickets[-1][0][1])
    
    return answer
