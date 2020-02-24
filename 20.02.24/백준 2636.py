N, M = list(map(int, input().split()))
arr = [list(map(int, input().split())) for i in range(N)]
cnt = M * N
result = 0
n = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 일단 복제
clone = []
for i in range(N):
    clone.append([])
    clone[i] = arr[i][:]

while True:
    # 다 녹았는지
    temp = 0
    cheese = 0
    for i in range(N):
        for j in range(M):
            if clone[i][j] == 0:
                temp += 1
            if clone[i][j] == 1:
                cheese += 1
    if cheese != 0:
        result = cheese
    if cnt == temp:
        break

    # 공기
    stack = [(0, 0)]
    clone[0][0] = 2
    while stack:
        x, y = stack.pop()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if clone[nx][ny] == 0:
                    stack.append((nx, ny))
                    clone[nx][ny] = 2

    # 공기 접촉부 
    for i in range(N):
        for j in range(M):
            if clone[i][j] == 1:
                x = i
                y = j
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if clone[nx][ny] == 2:
                        clone[x][y] = 3
                        break

    # 치즈 녹이고 다시 공기 0으로 바꿔주기
    for i in range(N):
        for j in range(M):
            if clone[i][j] != 1:
                clone[i][j] = 0

    # 시간
    n += 1


print(n)
print(result)