from collections import defaultdict
import sys; sys.stdin = open('1261.txt', 'r')

# import sys, heapq

# input = sys.stdin.readline
# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# for tc in range(1, int(input()) + 1):
#     M, N = map(int, input().split())
#     maze = [list(map(int, input().strip())) for _ in range(N)]

#     heap = []
#     dp = [[float('inf')] * M for _ in range(N)]
#     dp[0][0] = 0
#     heapq.heappush(heap, (0, 0, 0))
#     while heap:
#         x, y, AOJ = heapq.heappop(heap)
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < N and 0 <= ny < M:
#                 if maze[nx][ny] == 0:
#                     heapq.heappush(heap, (0, nx, ny))
#                     dp[nx][ny] = dp[x][y]
#                     continue
#                 else:
#                     heapq.heappush(heap, (1, nx, ny))
#                     dp[nx][ny] = min(dp[nx][ny], dp[x][y] + 1)
#         print(dp)



# false

# import sys, heapq
# from collections import defaultdict

# input = sys.stdin.readline
# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# for tc in range(1, int(input()) + 1):
#     M, N = map(int, input().split())
#     maze = [list(map(int, input().strip())) for _ in range(N)]

#     nodes = defaultdict(list)
#     for i in range(N):
#         for j in range(M):
#             for k in range(4):
#                 nx = i + dx[k]
#                 ny = j + dy[k]
#                 if 0 <= nx < N and 0 <= ny < M:
#                     nodes[str(i) + str(j)].append((str(nx) + str(ny), maze[nx][ny]))

#     distance = {str(i) + str(j): float('inf') for i in range(N) for j in range(M)}
#     heap = []
#     heapq.heappush(heap, (0, '00'))
#     distance['00'] = 0
#     while heap:
#         current_dis, current_node = heapq.heappop(heap)
#         for next_node, dis in nodes[current_node]:
#             if distance[next_node] > distance[current_node] + dis:
#                 distance[next_node] = distance[current_node] + dis
#                 heapq.heappush(heap, (distance[next_node], next_node))
    
#     answer = distance[str(N - 1) + str(M - 1)]
#     print(answer)



# dijkstra

# import sys, heapq

# input = sys.stdin.readline
# dx, dy = [-1, 1, 0, 0], [0, 0, -1 ,1]

# for tc in range(1, int(input()) + 1):
#     M, N = map(int, input().split())
#     maze = [list(map(int, input().strip())) for _ in range(N)]

#     distance = [[float('inf')] * M for _ in range(N)]
#     heap = []
#     heapq.heappush(heap, (0, 0, 0))
#     distance[0][0] = 0
#     while heap:
#         dis, x, y = heapq.heappop(heap)
#         if x == N - 1 and y == M - 1: break
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < N and 0 <= ny < M:
#                 if distance[nx][ny] > dis + maze[nx][ny]:
#                     distance[nx][ny] = dis + maze[nx][ny]
#                     heapq.heappush(heap, (distance[nx][ny], nx, ny))

#     print(distance[N - 1][M - 1])



# bfs

# import sys
# from collections import deque

# input = sys.stdin.readline
# dx, dy = [-1, 1, 0, 0], [0, 0, -1 ,1]

# for tc in range(1, int(input()) + 1):
#     M, N = map(int, input().split())
#     maze = [list(map(int, input().strip())) for _ in range(N)]

#     dp = [[float('inf')] * M for _ in range(N)]
#     deq = deque()
#     dp[0][0] = 0
#     deq.append((0, 0))
#     while deq:
#         x, y = deq.popleft()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < N and 0 <= ny < M:
#                 if dp[nx][ny] > dp[x][y] + maze[nx][ny]:
#                     dp[nx][ny] = dp[x][y] + maze[nx][ny]
#                     deq.append((nx, ny))
    
#     print(dp[N - 1][M - 1])




# 진짜 bfs

import sys
from collections import deque

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1 ,1]

for tc in range(1, int(input()) + 1):
    M, N = map(int, input().split())
    maze = [list(map(int, input().strip())) for _ in range(N)]

    dp = [[-1] * M for _ in range(N)]
    deq = deque()
    dp[0][0] = 0
    deq.append((0, 0))
    while deq:
        x, y = deq.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if dp[nx][ny] == -1:
                    if maze[nx][ny] == 0:
                        deq.appendleft([nx,ny])
                        dp[nx][ny] = dp[x][y]
                    elif maze[nx][ny] == 1:
                        deq.append([nx,ny])
                        dp[nx][ny] = dp[x][y] + 1
    
    print(dp[N - 1][M - 1])