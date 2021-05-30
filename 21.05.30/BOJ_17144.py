import sys; sys.stdin = open('17144.txt', 'r')

import sys

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def diffusion(R, C):
    dust_arr = [[0] * C for _ in range(R)]
    
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < R and 0 <= ny < C:
                        if arr[nx][ny] != -1:
                            dust_arr[nx][ny] += arr[i][j] // 5
                            cnt += 1
                if cnt:
                    dust_arr[i][j] += arr[i][j] - (arr[i][j] // 5) * cnt

    for i in range(R):
        for j in range(C):
            if dust_arr[i][j] > 0:
                arr[i][j] = dust_arr[i][j]
    return


def aircleaner(R, C, air_cleaner_point):
    top, bottom = air_cleaner_point
    down(R, *left(*up(*right(C, 0, *top))), top[0])
    up(*left(*down(R, *right(C, 0, *bottom))), bottom[0])
    return


def up(pre_dust, x, y, *limit_top):
    x -= 1
    while x > limit_top[0] if limit_top else x >= 0:
        current_dust = arr[x][y]
        arr[x][y] = pre_dust
        pre_dust = current_dust
        x -= 1
    return pre_dust, x + 1, y


def down(R, pre_dust, x, y, *limit_bottom):
    x += 1
    while x < limit_bottom[0] if limit_bottom else x < R:
        current_dust = arr[x][y]
        arr[x][y] = pre_dust
        pre_dust = current_dust
        x += 1
    return pre_dust, x - 1, y


def left(pre_dust, x, y):
    y -= 1
    while y >= 0:
        current_dust = arr[x][y]
        arr[x][y] = pre_dust
        pre_dust = current_dust
        y -= 1
    return pre_dust, x, y + 1


def right(C, pre_dust, x, y):
    y += 1
    while y < C:
        current_dust = arr[x][y]
        arr[x][y] = pre_dust
        pre_dust = current_dust
        y += 1
    return pre_dust, x, y - 1


for tc in range(1, int(input()) + 1):
    R, C, T = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(R)]

    air_cleaner_point = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] == -1:
                air_cleaner_point.append((i, j))

    for _ in range(T):
        diffusion(R, C)
        aircleaner(R, C, air_cleaner_point)

    answer = 0
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                answer += arr[i][j]

    print(answer)