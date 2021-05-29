import sys; sys.stdin = open('3055.txt', 'r')

# false

# from collections import deque
# import sys

# input = sys.stdin.readline
# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# for tc in range(1, int(input()) + 1):
#     R, C = map(int, input().split())
#     arr = [list(map(str, input()))[:C] for _ in range(R)]
    
#     waters_deq = deque()
#     # set start, end point
#     for i in range(R):
#         for j in range(C):
#             if arr[i][j] == 'S':
#                 start = (i, j)
#                 arr[i][j] = 0
#             elif arr[i][j] == 'D':
#                 end = (i, j)
#             elif arr[i][j] == '*':
#                 waters_deq.append((i, j))

#     water_dis = [[-1] * C for _ in range(R)]
#     # set start point
#     for x, y in waters_deq:
#         water_dis[x][y] = 0
#     # move waters
#     while waters_deq:
#         water_x, water_y = waters_deq.popleft()
#         for k in range(4):
#             wx = water_x + dx[k]
#             wy = water_y + dy[k]
#             if 0 <= wx < R and 0 <= wy < C:
#                 if arr[wx][wy] == '.' and water_dis[wx][wy] == -1:
#                     water_dis[wx][wy] = water_dis[water_x][water_y] + 1
#                     waters_deq.append((wx, wy))

#     # first move
#     deq = deque([start])
#     x, y = deq.popleft()
#     for k in range(4):
#         nx = x + dx[k]
#         ny = y + dy[k]
#         if 0 <= nx < R and 0 <= ny < C:
#             if arr[nx][ny] == '.':
#                 arr[nx][ny] = arr[x][y] + 1
#                 deq.append((nx, ny))

#     # move 
#     answer = 'KAKTUS'
#     while deq:
#         x, y = deq.popleft()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < R and 0 <= ny < C:
#                 # arrive end point
#                 if nx == end[0] and ny == end[1]:
#                     deq = []
#                     answer = arr[x][y] + 1
#                 # if move next point
#                 if arr[nx][ny] == '.' and arr[x][y] + 1 < water_dis[nx][ny]:
#                     arr[nx][ny] = arr[x][y] + 1
#                     deq.append((nx, ny))
    
#     print(answer)




# pass

import sys

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def move(answer, stack):
    tmp_stack = []
    for x, y in stack:
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < R and 0 <= ny < C:
                # arrive end point
                if nx == end[0] and ny == end[1]:
                    answer = arr[x][y] + 1
                    return answer, []
                # if move next point
                if arr[nx][ny] == '.':
                    arr[nx][ny] = arr[x][y] + 1
                    tmp_stack.append((nx, ny))
    return answer, tmp_stack


def move_waters(waters):
    tmp_waters = []
    for water_x, water_y in waters:
        for k in range(4):
            wx = water_x + dx[k]
            wy = water_y + dy[k]
            if 0 <= wx < R and 0 <= wy < C:
                if arr[wx][wy] == '.':
                    arr[wx][wy] = '*'
                    tmp_waters.append((wx, wy))
    return tmp_waters



for tc in range(1, int(input()) + 1):
    R, C = map(int, input().split())
    arr = [list(map(str, input()))[:C] for _ in range(R)]
    
    waters = []
    # set start, end point, water point
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'S':
                start = (i, j)
                arr[i][j] = 0
            elif arr[i][j] == 'D':
                end = (i, j)
            elif arr[i][j] == '*':
                waters.append((i, j))

    answer = 'KAKTUS'
    stack = [start]
    while stack:
        # move waters
        waters = move_waters(waters)

        # move 
        answer, stack = move(answer, stack)
    
    print(answer)




# answer
# 3
# KAKTUS
# 6
# 4
# 2
# 44