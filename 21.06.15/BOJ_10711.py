import sys; sys.stdin = open('10711.txt', 'r')

# time error

# import sys

# input = sys.stdin.readline
# dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

# def search_sand(H, W):
#     arr = [[0] * W for _ in range(H)]

#     for i in range(H):
#         for j in range(W):
#             if board[i][j].isnumeric():
#                 arr[i][j] = int(board[i][j])
#     return arr


# def wave(H, W):
#     corrosion = False
#     arr = [[0] * W for _ in range(H)]
    
#     for x in range(H):
#         for y in range(W):
#             if board[x][y]:
#                 sand_cnt = board[x][y]
#                 water_cnt = 0
#                 for k in range(8):
#                     nx = x + dx[k]
#                     ny = y + dy[k]
#                     if 0 <= nx < H and 0 <= ny < W:
#                         if board[nx][ny] == 0:
#                             water_cnt += 1
#                             if sand_cnt - water_cnt == 0: break
#                 else:
#                     arr[x][y] = sand_cnt
#                     continue

#                 arr[x][y] = 0
#                 corrosion = True

#     return corrosion, arr



# for tc in range(1, int(input()) + 1):
#     H, W = map(int, input().split())
#     board = [list(map(str, input())) for _ in range(H)]

#     board = search_sand(H, W)

#     answer = 0
#     while True:
#         flag, board = wave(H, W)
#         if flag:
#             answer += 1
#         else: break

#     print(answer)




# time error

# import sys
# from collections import deque

# input = sys.stdin.readline
# dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

# def search_waters(H, W):
#     waters = []
#     for i in range(H):
#         for j in range(W):
#             if board[i][j].isnumeric():
#                 board[i][j] = int(board[i][j])
#             else:
#                 board[i][j] = 0
#                 waters.append((i, j))
                
#     return waters



# for tc in range(1, int(input()) + 1):
#     H, W = map(int, input().split())
#     board = [list(map(str, input())) for _ in range(H)]

#     waters = search_waters(H, W)

#     answer = 0
#     while waters:
#         tmp_waters = []
#         answer += 1
#         for x, y in waters:
#             for k in range(8):
#                 nx = x + dx[k]
#                 ny = y + dy[k]
#                 if 0 <= nx < H and 0 <= ny < W:
#                     if board[nx][ny] > 0:
#                         board[nx][ny] -= 1
#                         if board[nx][ny] == 0:
#                             tmp_waters.append((nx, ny))
#         waters = tmp_waters

#     print(answer - 1)





# pypy

import sys
from collections import deque

input = sys.stdin.readline
dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

def search_waters(H, W):
    waters = deque()
    for i in range(H):
        for j in range(W):
            if board[i][j].isnumeric():
                board[i][j] = int(board[i][j])
            else:
                board[i][j] = 0
                waters.append((i, j))
                
    return waters



for tc in range(1, int(input()) + 1):
    H, W = map(int, input().split())
    board = [list(map(str, input())) for _ in range(H)]

    waters = search_waters(H, W)

    answer = 0
    cnt_list = [[0] * W for _ in range(H)]
    while waters:
        x, y = waters.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < H and 0 <= ny < W:
                if board[nx][ny]:
                    board[nx][ny] -= 1
                    if board[nx][ny] == 0:
                        waters.append((nx, ny))
                        cnt_list[nx][ny] = cnt_list[x][y] + 1
                        answer = max(answer, cnt_list[nx][ny])

    print(answer)