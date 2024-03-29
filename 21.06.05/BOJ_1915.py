import sys; sys.stdin = open('1915.txt', 'r')

# import sys

# input = sys.stdin.readline



# false


# N, M = map(int, input().split())
# arr = [list(map(int, input())) for _ in range(N)]

# answer = 0
# for i in range(N):
#     for j in range(M):
#         if arr[i][j]:
#             cnt = 1
#             flag = True
#             for p in range(min(N - i, M - j)):
#                 if flag == False: break
#                 for q in range(min(N - i, M - j)):
#                     print((i, j), (p, q), (i + p, j + q), cnt)
#                     if arr[i + p][j + q] == 0:
#                         flag = False
#                         break
#                 else: 
#                     cnt += 1
#             if cnt ** 2 > answer and flag:
#                 answer = cnt ** 2

# print(answer)



# time error

# import sys

# input = sys.stdin.readline

# def check(N, M, x, y, answer):
#     length = min(N - x, M - y)
    
#     max_hori = 0
#     while max_hori < length and arr[x][y + max_hori]:
#         max_hori += 1
    
#     for hori in range(1, max_hori):
#         tmp = 0
#         for k in range(hori):
#             sum_tmp = sum(arr[x + k][y:y + hori])
#             if sum_tmp == hori:
#                 tmp += sum_tmp
#             else: break
        
#         else: 
#             if tmp == hori ** 2 and tmp > answer:
#                 answer = tmp
    
#     return answer



# N, M = map(int, input().split())
# arr = [list(map(int, input().strip('\n'))) for _ in range(N)]

# answer = 0
# for i in range(N):
#     for j in range(M):
#         if arr[i][j]:
#             answer = check(N, M, i, j, answer)

# print(answer)



# dp

# dp리스트가 첫줄을 탐색할 때 -1해서 index가 엉키는거 아니냐 -> 어차피 탐색해본곳이 아니라 0이 최소값으로 나온다. 걱정 ㄴㄴ

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().strip('\n'))) for _ in range(N)]

dp = [[0] * M for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            if dp[i][j] > answer:
                answer = dp[i][j]

print(answer ** 2)