import sys; sys.stdin = open('1249.txt', 'r')

# false

# from collections import deque

# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# def bfs(arr, visited, S, G):
#     deq = deque([S])
#     while deq:
#         x, y = deq.popleft()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < N and 0 <= ny < N:
#                 # if [nx, ny] == G:
#                 #     if visited[nx][ny]:
#                 #         if visited[nx][ny] > visited[x][y]:
#                 #             visited[nx][ny] = visited[x][y]
#                 #     else:
#                 #         visited[nx][ny] = visited[x][y]
#                 if visited[nx][ny] == 0:
#                     visited[nx][ny] = visited[x][y] + arr[nx][ny]
#                     deq.append((nx, ny))
#                 else:
#                     if visited[nx][ny] > visited[x][y] + arr[nx][ny]:
#                         visited[nx][ny] = visited[x][y] + arr[nx][ny]
#                         deq.append((nx, ny))



# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     arr = list(list(map(int, input())) for _ in range(N))

#     visited = [[0] * N for _ in range(N)]
#     S, G = [0, 0], [N - 1, N - 1]
    
#     bfs(arr, visited, S, G)
#     answer = visited[G[0]][G[1]]

#     print(f'#{tc} {answer}')




#

# from collections import deque

# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# def bfs(arr, visited, S, G):
#     deq = deque([S])
#     while deq:
#         x, y = deq.popleft()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < N and 0 <= ny < N:
#                 if nx == 0 and ny == 0: continue
#                 elif visited[nx][ny] == 0:
#                     visited[nx][ny] = visited[x][y] + arr[nx][ny]
#                     deq.append((nx, ny))
#                 else:
#                     if visited[nx][ny] > visited[x][y] + arr[nx][ny]:
#                         visited[nx][ny] = visited[x][y] + arr[nx][ny]
#                         deq.append((nx, ny))



# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     arr = list(list(map(int, input())) for _ in range(N))

#     visited = [[0] * N for _ in range(N)]
#     S, G = [0, 0], [N - 1, N - 1]
    
#     bfs(arr, visited, S, G)
#     answer = visited[G[0]][G[1]]

#     # for i in range(N):
#     #     print(visited[i])

#     print(f'#{tc} {answer}')




#

# 다른 방법으로 처음 visited의 값을 매우 큰 값으로 설정해주고 비교해주며 update

from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(arr, visited, time, S, G):
    deq = deque([S])
    while deq:
        x, y = deq.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if nx == 0 and ny == 0: continue
                elif visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    time[nx][ny] = time[x][y] + arr[nx][ny]
                    deq.append((nx, ny))
                else:
                    if time[nx][ny] > time[x][y] + arr[nx][ny]:
                        time[nx][ny] = time[x][y] + arr[nx][ny]
                        deq.append((nx, ny))



for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(list(map(int, input())) for _ in range(N))

    visited = [[0] * N for _ in range(N)]
    time = [[0] * N for _ in range(N)]
    S, G = [0, 0], [N - 1, N - 1]
    
    bfs(arr, visited, time, S, G)
    answer = time[G[0]][G[1]]

    print(f'#{tc} {answer}')