import sys; sys.stdin = open('supply road.txt', 'r')


# dfs

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def go(x, y, time):
#     global res

#     if x == N - 1 and y == N -1:
#         if time < res:
#             res = time
#         return

#     for k in range(4):
#         nx = x + dx[k]
#         ny = y + dy[k]
#         if 0 <= nx < N and 0 <= ny < N:
#             if time + arr[nx][ny] > res:
#                 continue
#             else:
#                 if visited[nx][ny]:
#                     continue
#                 else:
#                     visited[nx][ny] = 1
#                     go(nx, ny, time + arr[nx][ny])
#                     visited[nx][ny] = 0



# for tc in range(1, int(input())+1):
#     N = int(input())
#     arr = [list(map(int, list(input()))) for _ in range(N)]
#     # print(arr)

#     res = 1000000
#     visited = [[0] * N for _ in range(N)]
#     visited[0][0] = 1
#     # print(visited)
#     go(0, 0, 0)

#     print(f'#{tc} {res}')


# # bfs
# from collections import deque

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# for tc in range(1, int(input())+1):
#     N = int(input())
#     arr = [list(map(int, list(input()))) for _ in range(N)]
    
#     for i in range(N):
#         for j in range(N):
#             arr[i][j] = [arr[i][j], 0]

#     que = deque()
#     que.append((0, 0))
#     while que:
#         x, y = que.popleft()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < N and 0 <= ny < N:
#                 if arr[nx][ny][1] == 0:
#                     arr[nx][ny][1] = arr[x][y][1] + arr[nx][ny][0]
#                     que.append((nx, ny))
#                 else:
#                     if arr[x][y][1] + arr[nx][ny][0] < arr[nx][ny][1]:
#                         arr[nx][ny][1] = arr[x][y][1] + arr[nx][ny][0]
#                         que.append((nx, ny))

#     # res = min(arr[N-2][N-1][1], arr[N-1][N-2][1])
#     res = arr[N-1][N-1][1]

#     print(f'#{tc} {res}')


# bfs2
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            arr[i][j] = [arr[i][j], 10000]

    que = deque()
    que.append((0, 0))
    arr[0][0][1] = 0
    while que:
        x, y = que.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[x][y][1] + arr[nx][ny][0] < arr[nx][ny][1]:
                    arr[nx][ny][1] = arr[x][y][1] + arr[nx][ny][0]
                    que.append((nx, ny))

    # res = min(arr[N-2][N-1][1], arr[N-1][N-2][1])
    res = arr[N-1][N-1][1]

    print(f'#{tc} {res}')