import sys; sys.stdin = open('text1.txt', 'r')
from collections import deque

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def check():
    res = 0
    q = deque()
    day_list = [[[0] * M for i in range(N)] for j in range(H)]

    for k in range(H):
        for i in range(N):
            for j in range(M):
                if arr[k][i][j] == 1:
                    q.append((i, j, k))
    
    temp = 0
    while q:
        x, y, z = q.popleft()
        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]
            nz = z + dz[k]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
                if arr[nz][nx][ny] == 0:
                    temp += 1
                    day_list[nz][nx][ny] = day_list[z][x][y] + 1
                    arr[nz][nx][ny] = 1
                    q.append((nx, ny, nz))

    day = 0
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if arr[k][i][j] == 0:         
                    return -1
                if day < day_list[k][i][j]:
                    day = day_list[k][i][j]
    return day



for tc in range(1, int(input()) + 1):
    M, N, H = map(int, input().split())
    arr = [[list(map(int, input().split())) for i in range(N)] for j in range(H)]

    res = check()
    print(res)