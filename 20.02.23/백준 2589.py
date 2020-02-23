# BFS

# N, M = list(map(int, input().split()))

# arr = [list(map(str, list(input()))) for i in range(N)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# for i in range(N):
#     for j in range(M):
#         clone = []
#         for i in range(N):
#             clone.append([])
#             clone[i] = arr[i][:]
#         if clone[i][j] == 'L':
#             que = []
#             x = i
#             y = j
#             cnt = 0
#             result = 0
#             clone[x][y] = 'W'
#             que.append((x, y))
#             while que:
#                 x, y = que.pop(0)
#                 for k in range(4):
#                     nx = x + dx[k]
#                     ny = y + dy[k]
#                     if 0 <= nx < N and 0 <= ny < M:
#                         if clone[nx][ny] == 'L':
#                             que.append((nx, ny))
#                             clone[nx][ny] = 'W'
#                             cnt += 1
#                 if cnt > result:
#                     result = cnt

# print(result)

# N, M = list(map(int, input().split()))

# arr = [list(map(str, list(input()))) for i in range(N)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# final = 0
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 'L':
#             que = []
#             visit = [[0] * M for i in range(N)]
#             x = i
#             y = j
#             result = 0
#             visit[x][y] = 1
#             que.append((x, y))
#             while que:
#                 x, y = que.pop(0)
#                 for k in range(4):
#                     nx = x + dx[k]
#                     ny = y + dy[k]
#                     if 0 <= nx < N and 0 <= ny < M:
#                         if arr[nx][ny] == 'L' and visit[nx][ny] == 0:
#                             que.append((nx, ny))
#                             visit[nx][ny] = visit[x][y] + 1              
#                             if  visit[nx][ny] > result:
#                                 result = visit[nx][ny]
#             if result > final:
#                 final = result

# print(final-1)

# collection 사용
import collections

N, M = list(map(int, input().split()))

arr = [list(map(str, list(input()))) for i in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

final = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            que = collections.deque()
            visit = [[0] * M for i in range(N)]
            x = i
            y = j
            result = 0
            visit[x][y] = 1
            que.append((x, y))
            while que:
                x, y = que.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        if arr[nx][ny] == 'L' and visit[nx][ny] == 0:
                            que.append((nx, ny))
                            visit[nx][ny] = visit[x][y] + 1              
                            if  visit[nx][ny] > result:
                                result = visit[nx][ny]
            if result > final:
                final = result

print(final-1)