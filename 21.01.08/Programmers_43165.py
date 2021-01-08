# recursive solve

# def solution(numbers, target):
#     global answer
#     answer = 0
#     recursive(numbers, target, 0, 0)
#     return answer


# def recursive(numbers, target, cnt, val):
#     global answer

#     if cnt == len(numbers):
#         if val == target:
#             answer += 1
#         return
        

#     recursive(numbers, target, cnt + 1, val + numbers[cnt])
#     recursive(numbers, target, cnt + 1, val - numbers[cnt])



# product module

from itertools import product

def solution(numbers, target):
    lst = [[x, -x] for x in numbers]
    sum_lst = list(map(sum, product(*lst)))
    return sum_lst.count(target)




print(solution([1, 1, 1, 1, 1], 3))

# answer
# 5