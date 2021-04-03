# false

# def solution(arr):
#     answer = float('inf')

#     for i in range(min(arr), 0, -1):
#         cnt = 0
#         for val in arr:
#             if val % i == 0:
#                 cnt += 1
#         if cnt == len(arr):
#             tmp = i
#             for val in arr:
#                 tmp *= val // i
#             if tmp < answer:
#                 answer = tmp

#     return answer


# false

def solution(arr):
    answer = float('inf')

    results = []
    for i in range(min(arr), 0, -1):
        for val in arr:
            tmp = i
            if val % i == 0:
                tmp *= val // i
            else:
                tmp *= val
        results.append(tmp)
            
    answer = min(results)

    return answer




print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))
print(solution([3, 4, 9, 16]))

# answer
# 168
# 6
# 144