import sys; sys.stdin = open('square room.txt', 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    now = 0
    res = 0
    for i in range(N):
        for j in range(N):
            now = arr[i][j]
            stack = [(i, j)]
            temp = 0
            while stack:
                x, y = stack.pop()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if arr[nx][ny] == now + 1:
                            