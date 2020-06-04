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

