import sys; sys.stdin = open("maze distance.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# for tc in range(1, int(input())+1):
#     N = int(input())
#     arr = [list(map(int, list(input()))) for _ in range(N)]
    
#     res = 0
#     for i in range(N):
#         if res == 0:
#             for j in range(N):
#                 if arr[i][j] == 2:
#                     stack = [(i, j)]
#                     dis = 0
#                     arr[i][j] = 1
#                     temp = 1
#                     while stack:
#                         for _ in range(temp):
#                             temp = 0
#                             x, y = stack.pop()
#                             for k in range(4):
#                                 nx = x + dx[k]
#                                 ny = y + dy[k]
#                                 if 0 <= nx < N and 0 <= ny < N:
#                                     if arr[nx][ny] == 3:
#                                         stack.clear()
#                                         res = 1
#                                         break
#                                     elif arr[nx][ny] == 0:
#                                         stack.append((nx, ny))
#                                         arr[nx][ny] = 1
#                                         temp += 1
#                         dis += 1

#     if res == 1:
#         print(f'#{tc} {dis}')
#     else:
#         print(f'#{tc} {res}')

#
for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    res = 0
    for i in range(N):
        if res == 0:
            for j in range(N):
                if arr[i][j] == '2':
                    stack = [(i, j)]
                    arr[i][j] = 1
                    cnt = 0
                    dis = 0
                    while stack:
                        x, y = stack.pop()
                        cnt = arr[x][y] + 1
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if 0 <= nx < N and 0 <= ny < N:
                                if arr[nx][ny] == '3':
                                    res = 1
                                    dis = arr[x][y] - 1
                                elif arr[nx][ny] == '0':
                                    stack.append((nx, ny))
                                    arr[nx][ny] = cnt
                    break
        else: break
              
    if res:
        print(f'#{tc} {dis}')
    else:
        print(f'#{tc} {res}')