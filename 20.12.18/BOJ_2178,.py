import sys; sys.stdin = open('text1.txt', 'r')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q = deque()
    q.append(start)

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == '1':
                    if nx == N - 1 and ny == M - 1:
                        res_list[nx][ny] = res_list[x][y] + 1
                        return
                    elif res_list[nx][ny] == 0:
                        res_list[nx][ny] = res_list[x][y] + 1
                        q.append((nx, ny))



for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    res_list = [[0] * M for _ in range(N)]
    start = (0, 0)
    bfs()
    print(res_list[N - 1][M - 1] + 1)