# time error

# from itertools import permutations
# import math

# def solution(numbers):
#     answer = 0

#     pers_lst = [list(permutations(numbers, x)) for x in range(1, len(numbers) + 1)]
#     pers = set()
#     for i in range(len(pers_lst)):
#         for j in range(len(pers_lst[i])):
#             tem = ''
#             for k in range(len(pers_lst[i][j])):
#                 tem += pers_lst[i][j][k]
#             pers.add(int(tem))
    
#     pers.discard(0)
#     pers.discard(1)

#     # 소수 판별(에라토스테네스의 체)
#     check = [True for i in range(max(pers) + 1)]
#     for i in range(2, int(math.sqrt(max(pers) + 1))):
#         if check[i] == True:
#             j = 2
#             while i * j <= max(pers):
#                 check[i * j] = False
#                 j += 1
    
#     for per in pers:
#         if check[per]:
#             answer += 1

#     return answer



from itertools import permutations

def solution(numbers):
    answer = 0

    pers_lst = [list(permutations(numbers, x)) for x in range(1, len(numbers) + 1)]
    pers = set()
    for i in range(len(pers_lst)):
        for j in range(len(pers_lst[i])):
            tem = ''
            for k in range(len(pers_lst[i][j])):
                tem += pers_lst[i][j][k]
            pers.add(int(tem))
    
    pers.discard(0)
    pers.discard(1)

    answer = len(pers)
    for per in pers:
        for i in range(2, int(per ** 0.5) + 1):
            if per % i == 0:
                answer -= 1
                break

    return answer



print(solution("17"))
print(solution("011"))