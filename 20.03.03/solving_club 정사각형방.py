import sys
sys.stdin = open("정사각형방.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]

    start = 0
    result = 0
    for i in range(N):
        for j in range(N):
            temp = 1
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if arr[nx][ny] == arr[x][y] + 1:
                            stack.append((nx, ny))
                            temp += 1
            if temp > result:
                result = temp
                start = arr[i][j]
            elif temp == result:
                if start > arr[i][j]:
                    start = arr[i][j]
            
    print(f'#{t+1} {start} {result}')