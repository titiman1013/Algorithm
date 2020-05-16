import sys; sys.stdin = open('laboratory.txt', 'r')
from itertools import combinations
from collections import deque
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def wall_create(wall):
    global arr_copy
    arr_copy = copy.deepcopy(arr)
    # print(arr_copy)
    for x, y in wall:
        arr_copy[x][y] = 1
    # print(arr_copy)
    return arr_copy


def diffusion():
    global virus_zone

    que = deque()
    for i in range(len(virus)):
        que.append(virus[i])
    
    cnt = 0
    while que:
        x, y = que.popleft()
        if virus_zone:
            if cnt > virus_zone:
                return
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if arr_copy[nx][ny] == 0:
                    arr_copy[nx][ny] = 2
                    que.append((nx, ny))
    
    virus_zone = cnt


def safety_zone_counter():
    global res

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr_copy[i][j] == 0:
                cnt += 1
    if cnt > res:
        res = cnt


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    empty = []
    virus = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                empty.append((i, j))
            if arr[i][j] == 2:
                virus.append((i, j))

    wall = list(combinations(empty, 3))
    res = 0
    virus_zone = 0
    arr_copy = []
    for i in range(len(wall)):
        wall_create(wall[i])
        # print(arr_copy)
        diffusion()
        safety_zone_counter()

    print(f'#{tc} {res}')