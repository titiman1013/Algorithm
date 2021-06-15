import sys; sys.stdin = open('10711.txt', 'r')

# time error

import sys

input = sys.stdin.readline
dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

def search_sand(H, W):
    arr = [[0] * W for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if board[i][j].isnumeric():
                arr[i][j] = int(board[i][j])
    return arr


def wave(H, W):
    corrosion = False
    arr = [[0] * W for _ in range(H)]
    
    for x in range(H):
        for y in range(W):
            if board[x][y]:
                sand_cnt = board[x][y]
                water_cnt = 0
                for k in range(8):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < H and 0 <= ny < W:
                        if board[nx][ny] == 0:
                            water_cnt += 1
                            if sand_cnt - water_cnt == 0: break
                else:
                    arr[x][y] = sand_cnt
                    continue
 
                arr[x][y] = 0
                corrosion = True

    return corrosion, arr
 


for tc in range(1, int(input()) + 1):
    H, W = map(int, input().split())
    board = [list(map(str, input())) for _ in range(H)]

    board = search_sand(H, W)

    answer = 0
    while True:
        flag, board = wave(H, W)
        if flag:
            answer += 1
        else: break

    print(answer)