import sys; sys.stdin = open("tomato.txt", "r")
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(1, int(input())+1):
    M, N = map(int, input().split())
    # M 은 가로, N 은 세로
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 익토 1, 안익토 0, 빈칸 -1

    dq = deque([])
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                dq.append((i, j))
    
    while dq:
        x, y = dq.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0:
                    dq.append((nx, ny))
                    arr[nx][ny] = arr[x][y] + 1
    
    day = 0
    for i in range(N):
        if day == -1:
            break
        for j in range(M):
            if arr[i][j] == 0:
                day = -1
                break
            elif arr[i][j] > day:
                day = arr[i][j]

    # print(arr)
    if day == -1:
        # print(f'#{tc} {day}')
        print(day)
    else:
        # print(f'#{tc} {day-1}')
        print(day-1)

# 답 
#1 8
#2 -1
#3 6
#4 14
#5 0