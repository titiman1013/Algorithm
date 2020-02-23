N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


result = 0
for rain in range(101):
    cnt = 0
    clone = []
    for i in range(len(arr)):
        clone.append([])
        clone[i] = arr[i][:]
    for i in range(N):
        for j in range(N):
            if clone[i][j] > rain:
                cnt += 1
                clone[i][j] = 0
                x = i
                y = j
                stack = [(x, y)]
                while stack:
                    x, y = stack.pop()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N:
                            if clone[nx][ny] > rain:
                                stack.append((nx,ny))
                                clone[nx][ny] = 0
                            
    if cnt > result:
        result = cnt

print(result)