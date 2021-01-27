# from collections import deque

# def solution(n, lost, reserve):
#     answer = n - len(lost)

#     lost.sort()
#     reserve.sort()

#     for p in reserve:
#         if p in lost:
#             reserve.remove(p)
#             lost.remove(p)
#             answer += 1
            
#     deq = deque(lost)
#     while deq:
#         p = deq.popleft()
#         if p - 1 in reserve:
#             reserve.remove(p - 1)
#             answer += 1
#         elif p + 1 in reserve:
#             reserve.remove(p + 1)
#             answer += 1

#     return answer



#

# def solution(n, lost, reserve):
#     answer = 0

#     reserve_set = set(reserve) - set(lost)
#     lost_set = set(lost) - set(reserve)

#     for p in reserve_set:
#         if p - 1 in lost_set:
#             lost_set.remove(p - 1)
#         elif p + 1 in lost_set:
#             lost_set.remove(p + 1)

#     return answer + n - len(lost_set)

def solution(n, lost, reserve):
    answer = 0

    reserve = set(reserve) - set(lost)
    lost = set(lost) - set(reserve)
    print(reserve, lost)

    for p in reserve:
        if p - 1 in lost:
            lost.remove(p - 1)
        elif p + 1 in lost:
            lost.remove(p + 1)

    return answer + n - len(lost)





print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
print(solution(3, [1, 2], [2, 3]))

# answer
# 5
# 4
# 2