import sys; sys.stdin = open('robotic vacuum.txt', 'r')

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    now_x, now_y, direction = map(int, input().split())
    # 0: 북, 1: 동, 2: 남, 3: 서
    arr = [list(map(int, input().split())) for _ in range(N)]

    res = 0
    stack = [(now_x, now_y, direction)]
    while stack:
        x, y, direction = stack.pop()
        arr[x][y] = 2
        res += 1
        cnt = 0
        for k in range(direction, direction-4, -1):
            # if k > 3:
            #     k -= 4
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0:
                    stack.append((nx, ny, k))
                    cnt += 1
        if cnt == 0:
            if arr[x-dx[direction]][y-dx[direction]] == 2:
                stack.append((x-dx[direction], y-dx[direction], direction))
            elif arr[x-dx[direction]][y-dx[direction]] == 1:
                break
        print(res)
        

    print(f'#{tc} {res}')