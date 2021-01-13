# from collections import deque

# def solution(priorities, location):
#     order_lst = []

#     N = len(priorities)
#     d_p = deque(priorities)
#     d_o = deque(i for i in range(N))

#     while d_p:
#         if len(d_p) == 1:
#             order_lst.append(d_o[0])
#             break

#         prior = d_p.popleft()
#         order_num = d_o.popleft()
#         if prior >= max(d_p):
#             order_lst.append(order_num)
#         else:
#             d_p.append(prior)
#             d_o.append(order_num)

#     for idx, val in enumerate(order_lst):
#         if val == location:
#             answer = idx + 1
#             break

#     return answer



# best solve
from collections import deque

def solution(priorities, location):
    answer = 0
    deq = deque((i, p) for i, p in enumerate(priorities))
    while True:
        cur = deq.popleft()
        if any(cur[1] < d[1] for d in deq):
            deq.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer




print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))