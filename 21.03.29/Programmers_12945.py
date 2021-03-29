#

# def solution(n):
#     a, b = 0, 1
#     for i in range(n):
#         a, b = b, a + b
#     return a



#

def solution(n):
    answer = 0

    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i - 2] + dp[i - 1])

    answer = dp[n] % 1234567

    return answer




print(solution(3))
print(solution(5))

# answer
# 2
# 5