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

# def solution(arr):
#     answer = float('inf')

#     results = []
#     for i in range(min(arr), 0, -1):
#         for val in arr:
#             tmp = i
#             if val % i == 0:
#                 tmp *= val // i
#             else:
#                 tmp *= val
#         results.append(tmp)
            
#     answer = min(results)

#     return answer


# false

# def calc(arr, i):
#     for idx, val in enumerate(arr):
#         if val % i == 0:
#             arr[idx] = val // i

#     result = i
#     for val in arr:
#         result *= val
    
#     return result


# def solution(arr):
#     answer = float('inf')

#     for i in range(2, max(arr) + 1):
#         cnt = 0
#         for val in arr:
#             if val % i == 0:
#                 cnt += 1
#         if cnt >= 2:
#             tmp = calc(arr, i)
#             if tmp < answer:
#                 answer = tmp
    
#     if answer == float('inf'):
#         answer = calc(arr, 1)

#     return answer


# clear

def GCD(num1, num2):
    x, y = min(num1, num2), max(num1, num2)
    while y:
        x, y = y, x % y
    return x


def LCM(num1, num2):
    x, y = min(num1, num2), max(num1, num2)
    res = (x * y) // GCD(x, y)
    return res


def solution(arr):
    answer = 0

    while len(arr) > 1:
        a, b = arr.pop(), arr.pop()
        arr.append(LCM(a, b))

    answer = arr[0]

    return answer





print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))
print(solution([3, 4, 9, 16]))

# answer
# 168
# 6
# 144