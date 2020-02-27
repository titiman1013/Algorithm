import sys
sys.stdin = open("행렬찾기.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    
    result = []
    num = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                num += 1
                temp = [(i, j)] # 좌표 임시로 넣어두는 곳
                stack = [(i, j)]
                arr[i][j] = 0
                while stack:
                    x, y = stack.pop()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N:
                            if arr[nx][ny] != 0:
                                stack.append((nx, ny))
                                temp.append((nx, ny))
                                arr[nx][ny] = 0
                a, b = max(temp)
                c, d = min(temp)
                result.append((a-c+1, b-d+1))

    result.sort()
    for j in range(len(result)-1, 0, -1):
        for i in range(len(result)-1, 0, -1):
            while result[i][0] * result[i][1] < result[i-1][0] * result[i-1][1]:
                a = result[i]
                b = result[i-1]
                result[i] = b
                result[i-1] = a

    print(f'#{t+1}', end = ' ')
    print(num, end = ' ')
    for i in range(len(result)):
        print(*result[i], end = ' ')
    print()