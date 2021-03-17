# false

# def solution(land):
#     answer = 0

#     pos = -1
#     for row_idx in range(len(land)):
#         max_idx = -1
#         max = 0
#         for col_idx, num in enumerate(land[row_idx]):
#             if num > max and col_idx != pos:
#                 max_idx, max = col_idx, num
#         pos = max_idx
#         answer += max
    
#     return answer


# dp

def solution(land):
    answer = 0

    dp = [[0] * 4 for _ in range(len(land))]
    dp[0] = land[0]
    for i in range(1, len(land)):
        for j in range(len(land[i])):
            if j:
                if j < len(land[i]) - 1:
                    dp[i][j] = max(max(dp[i - 1][:j]), max(dp[i - 1][j + 1:])) + land[i][j]
                else:
                    dp[i][j] = max(dp[i - 1][:j]) + land[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j + 1:]) + land[i][j]
    answer = max(dp[-1])

    return answer




print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))

# answer
# 16