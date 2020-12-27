import sys; sys.stdin = open('text1.txt', 'r')
from collections import deque

# 10시로 다시풀기

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def water(arr_clone, temp):
    q = deque()
    for i in range(R):
        for j in range(C):
            if arr_clone[i][j] == '*':
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < R and 0 <= ny < C:
                if arr_clone[nx][ny] == '.':
                    arr_clone[nx][ny] = '*'
                    temp[nx][ny][0] = temp[x][y][0] + 1
                    q.append((nx, ny))
    return temp


def move(arr_clone, temp, start):
    q = deque()
    q.append(start)
    
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < R and 0 <= ny < C:
                if arr_clone[nx][ny] == '.':
                    arr_clone[nx][ny] = -1
                    temp[nx][ny][1] = temp[x][y][1] + 1
                    q.append((nx, ny))
    return temp


def check(arr_clone):
    for i in range(R):
        for j in range(C):
            if arr_clone[i][j] == 'S':
                start = [i, j]
            elif arr_clone[i][j] == 'D':
                goal = [i, j]

    calc_list = [[[0, 0] for i in range(C)] for j in range(R)]
    
    calc_list = water(arr_clone, calc_list)
    calc_list = move(arr_clone, calc_list, start)

    X, Y = calc_list[goal[0]][goal[1]]
    print(X, Y)
    return



for tc in range(1, int(input()) + 1):
    R, C = map(int, input().split())
    arr = [list(map(str, list(input()))) for _ in range(R)]

    res = check(arr)
    print(res)