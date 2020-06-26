import sys; sys.stdin = open('maze.txt', 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for T in range(1, 11):
    tc = int(input())
    arr = [list(map(int, list(input()))) for _ in range(16)]

    stack = [(1, 1)]
    res = 0
    while stack:
        x, y = stack.pop()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 16 and 0 <= ny < 16:
                if arr[nx][ny] == 0:
                    stack.append((nx, ny))
                    arr[nx][ny] = 2
                elif arr[nx][ny] == 3:
                    stack.clear()
                    res = 1

    print(f'#{tc} {res}')