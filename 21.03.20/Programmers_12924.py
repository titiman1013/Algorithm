# def solution(n):
#     answer = 1

#     for i in range(1, n // 2 + 1):
#         temp = 0
#         for j in range(i, n + 1):
#             temp += j
#             if temp == n:
#                 answer += 1
#                 break
#             elif temp > n: break

#     return answer


# 등차수열 합 공식

def solution(n):
    return len([i for i in range(1, n + 1, 2) if n % i is 0])




print(solution(15))

# answer
# 4