# N, M = list(map(int, input().split()))
# arr = [list(map(int, input().split())) for i in range(N)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# # clone = []
# # for i in range(N):
# #     clone.append([])
# #     clone[i] = arr[i][:]

# num = 0 # 빙산 덩어리 개수
# year = 0 # 걸리는 연도
# while True:
#     # 빙산 개수 세기
#     visit = [list([False] * M) for i in range(N)]
#     num = 0
#     a = 0
#     for i in range(N):
#         if a != 0:
#             break
#         for j in range(M):
#             if arr[i][j] != 0 and visit[i][j] == False:
#                 stack = [(i, j)]
#                 visit[i][j] = True
#                 while stack:
#                     x, y = stack.pop()
#                     for k in range(4):
#                         nx = x + dx[k]
#                         ny = y + dy[k]
#                         if 0 <= nx < N and 0 <= ny < M:
#                             if arr[nx][ny] != 0 and visit[nx][ny] == False:
#                                 visit[nx][ny] = True
#                                 stack.append((nx, ny))
#                 num += 1
#                 if num > 1:
#                     a += 1
#                     break

#     # 빙산 개수 판단
#     if num > 1:
#         break

#     # 빙산 녹이는거
#     a_ = 0
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] != 0:
#                 cnt = 0
#                 x = i
#                 y = j
#                 for k in range(4):
#                     nx = x + dx[k]
#                     ny = y + dy[k]
#                     if 0 <= nx < N and 0 <= ny < M:
#                         if arr[nx][ny] == 0:
#                             cnt += 1
#                 if arr[i][j] - cnt < 0:
#                     arr[i][j] = '0'
#                     a_ += 1
#                 else:
#                     arr[i][j] = str(arr[i][j]-cnt)
#                     a_ += 1

#     # 다시 숫자로 바꿔줌
#     b = 0
#     for i in range(N):
#         if b != 0:
#             break
#         for j in range(M):
#             if type(arr[i][j]) is not int:
#                 arr[i][j] = int(arr[i][j])
#                 a_ -= 1
#                 if a_ == 0:
#                     b += 1
#                     break

        
#     year += 1

# print(year)















# N, M = list(map(int, input().split()))
# arr = [list(map(int, input().split())) for i in range(N)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# # clone = []
# # for i in range(N):
# #     clone.append([])
# #     clone[i] = arr[i][:]

# num = 0 # 빙산 덩어리 개수
# year = 0 # 걸리는 연도
# while True:
#     n = 0
#     # 빙산 개수 세기
#     visit = [list([False] * M) for i in range(N)]
#     num = 0
#     a = 0
#     for i in range(N):
#         if a != 0:
#             break
#         for j in range(M):
#             if arr[i][j] > 0 and visit[i][j] == False:
#                 stack = [(i, j)]
#                 visit[i][j] = True
#                 while stack:
#                     x, y = stack.pop()
#                     for k in range(4):
#                         nx = x + dx[k]
#                         ny = y + dy[k]
#                         if 0 <= nx < N and 0 <= ny < M:
#                             if arr[nx][ny] > 0 and visit[nx][ny] == False:
#                                 visit[nx][ny] = True
#                                 stack.append((nx, ny))
#                 num += 1
#                 if num > 1:
#                     a += 1
#                     break

#     # 빙산 개수 판단
#     if num > 1:
#         break

#     # 빙산 녹이는거
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] > 0:
#                 cnt = 0
#                 x = i
#                 y = j
#                 for k in range(4):
#                     nx = x + dx[k]
#                     ny = y + dy[k]
#                     if 0 <= nx < N and 0 <= ny < M:
#                         if arr[nx][ny] == 0:
#                             cnt += 1
#                         if arr[nx][ny] == n and n == 0:
#                             cnt += 1
#                 if arr[i][j] - cnt == 0:
#                     n = -1
#                     arr[i][j] = n
#                 else:
#                     arr[i][j] = arr[i][j]-cnt
#     print(arr)

        
#     year += 1

# print(year)
# print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')







N, M = list(map(int, input().split()))
arr = [list(map(int, input().split())) for i in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# clone = []
# for i in range(N):
#     clone.append([])
#     clone[i] = arr[i][:]

num = 0 # 빙산 덩어리 개수
year = 0 # 걸리는 연도
while True:
    # 빙산 개수 세기
    visit = [list([False] * M) for i in range(N)]
    num = 0
    a = 0
    for i in range(N):
        if a != 0:
            break
        for j in range(M):
            if arr[i][j] == -10000:
                arr[i][j] = 0 
            if arr[i][j] != 0 and visit[i][j] == False:
                stack = [(i, j)]
                visit[i][j] = True
                while stack:
                    x, y = stack.pop()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < M:
                            if arr[nx][ny] == -10000:
                                arr[nx][ny] = 0 
                            if arr[nx][ny] != 0 and visit[nx][ny] == False:
                                visit[nx][ny] = True
                                stack.append((nx, ny))
                num += 1
                if num > 1:
                    a += 1
                    break

    # 빙산 개수 판단
    if num > 1:
        break

    # 빙산 녹이는거
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                cnt = 0
                x = i
                y = j
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        if arr[nx][ny] == 0:
                            cnt += 1
                if arr[i][j] - cnt <= 0:
                    arr[i][j] = -10000
                else:
                    arr[i][j] = arr[i][j]-cnt
        
    year += 1

print(year)