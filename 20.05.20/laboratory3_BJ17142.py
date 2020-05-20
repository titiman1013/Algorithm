import sys; sys.stdin = open('laboratory3.txt', 'r')
from collections import deque
from itertools import combinations
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# def check(virus, wall):
#     global res

#     lab = [[0] * N for _ in range(N)]
#     for i in range(len(virus_list)):
#         lab[virus_list[i][0]][virus_list[i][1]] = '0'
#     # for i in range(len(virus)):
#     #     lab[virus[i][0]][virus[i][1]] = '2'
#     for i in range(len(wall)):
#         lab[wall[i][0]][wall[i][1]] = '1'
    
#     que = deque()
#     for i in range(len(virus)):
#         que.append(virus[i])

#     cnt = 0
#     while que:
#         x, y = que.popleft()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < N and 0 <= ny < N:
#                 if lab[nx][ny] == 0 or lab[nx][ny] == '0':
#                     # print((nx, ny))
#                     if lab[x][y] == '0':
#                         lab[nx][ny] = 1
#                         que.append((nx, ny))
#                     else:
#                         lab[nx][ny] = lab[x][y] + 1
#                         que.append((nx, ny))
#                         if lab[nx][ny] > cnt:
#                             cnt = lab[nx][ny]
#                             # if cnt > res:
#                             #     return
#                 # elif lab[nx][ny] == '0':
#                 #     for k in range(4):
#                 #         tx = nx + dx[k]
#                 #         ty = ny + dy[k]
#                 #         if 0 <= tx < N and 0 <= ty < N:
#                 #             if lab[tx][ty] == 0:
#                 #                 lab[tx][ty] = lab[x][y] + 1
#                 #                 que.append((tx, ty))
#                 #                 if lab[tx][ty] > cnt:
#                 #                     cnt = lab[tx][ty]
#                                     # if cnt > res:
#                                     #     return
#         if lab[x][y] == '0':
#             lab[x][y] = '2'

#     for i in range(N):
#         for j in range(N):
#             if lab[i][j] == 0:
#                 cnt = -1
#                 return cnt

#     # if res > cnt:
#     #     print(lab)

#     return cnt



# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     # 0: 빈 칸, 1: 벽, 2: 바이러스

#     virus_list = []
#     wall_list = []
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 2:
#                 virus_list.append((i, j))
#             elif arr[i][j] == 1:
#                 wall_list.append((i, j))

#     pick_virus = list(combinations(virus_list, M))
    
#     res = 100000
#     for i in range(len(pick_virus)):
#         temp = check(pick_virus[i], wall_list)
#         if temp:
#             if res > temp:
#                 res = temp
    
#     if res == 100000:
#         res = 0
            
#     print(f'#{tc} {res}')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    