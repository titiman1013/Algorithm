import sys; sys.stdin = open('text1.txt', 'r')
from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def search_shark():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                return (i, j)


def bfs(pos):
    global size, ate

    dis_lst = [[0] * N for _ in range(N)]
    deq = deque()
    deq.append(pos)
    while deq:
        x, y = deq.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx == pos[0] and ny == pos: continue
            if 0 <= nx < N and 0 <= ny < N and dis_lst[nx][ny] == 0 and size >= arr[nx][ny]:
                dis_lst[nx][ny] = dis_lst[x][y] + 1
                deq.append((nx, ny))

    dis = 1000
    point = []
    for i in range(N):
        for j in range(N):
            if 0 < dis_lst[i][j] < dis and 0 < arr[i][j] < size:
                dis = dis_lst[i][j]
                point = (i, j)
    print(point)




for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    pos = search_shark()

    sec = 0
    size = 2
    ate = 0
    bfs(pos)
    # while True: