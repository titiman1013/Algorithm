import sys; sys.stdin = open('baby shark.txt', 'r')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    que = deque()

    for i in range(N):
        for j in range(N):
            arr[i][j] = [arr[i][j], 0]

    shark_size = 2
    shark_eat = 0
    while True:
        for i in range(N):
            for j in range(N):
                if arr[i][j][0] == 9:
                    que.append((i, j))
                    arr[i][j][0] = 0
                    cnt = 0
                    while que:
                        x, y = que.popleft()
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if 0 <= nx < N and 0 <= ny < N:
                                if arr[nx][ny][0]:
                                    if arr[nx][ny][0] < shark_size:
                                        shark_eat += 1
                                        arr[nx][ny][0] = 9
                                        arr[nx][ny][1] = arr[x][y][1] + 1
                                        cnt += 1
                                        if shark_size == shark_eat:
                                            shark_size += 1
                                            shark_eat = 0
                                        res = arr[nx][ny][1]
                                        que.clear()
                                        que.append((nx, ny))
                                        break

                                    elif arr[nx][ny][0] == shark_size:
                                        arr[nx][ny][1] = arr[x][y][1] + 1
                                        que.append((nx, ny))
                                elif arr[nx][ny][0] == 0:
                                    arr[nx][ny][1] = arr[x][y][1] + 1
                                    que.append((nx, ny))
        if cnt == 0:
            break
    
    print(f'#{tc} {res}')