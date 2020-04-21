dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
arr = [list(map(str, list(input()))) for _ in range(N)]
# print(arr)
res_rgb = 0
for i in range(N):
    for j in range(N):
        if type(arr[i][j]) == str:
            temp = arr[i][j]
            # print(temp)
            res_rgb += 1
            stack = [(i, j)]
            if arr[i][j] == 'R' or arr[i][j] == 'G':
                arr[i][j] = 1
            else:
                arr[i][j] = 0
            while stack:
                x, y = stack.pop()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if arr[nx][ny] == temp:
                            stack.append((nx, ny))
                            if arr[nx][ny] == 'R' or arr[nx][ny] == 'G':
                                arr[nx][ny] = 1
                            else:
                                arr[nx][ny] = 0
        # print(arr)
# print(res_rgb)
res_rb = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 or arr[i][j] == 0:
            temp = arr[i][j]
            res_rb += 1
            stack = [(i, j)]
            arr[i][j] = -1
            while stack:
                x, y = stack.pop()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if arr[nx][ny] == temp:
                            stack.append((nx, ny))
                            arr[nx][ny] = -1

print(res_rgb, res_rb)

#
# 5
# RRRBB
# GGBBB
# BBBRR
# BBRRR
# RRRRR