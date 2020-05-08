import sys; sys.stdin = open('dice rolling.txt', 'r')

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for tc in range(1, int(input())+1):
    N, M, x, y, K = map(int, input().split())
    # N: 세로, M: 가로, K: 명령개수
    arr = [list(map(int, input().split())) for _ in range(N)]
    orders = list(map(int, input().split()))
    # 동:1, 서:2, 북:3, 남:4

    print(f'#{tc}')
    dice = [0] * 6   # 바닥-남-위-북-서-남
    # dice_position = 0   # 바닥이 시작점

    for order in orders:
        if order == 1:
            nx = x + dx[order-1]
            ny = y + dy[order-1]
            if 0 <= nx < N and 0 <= ny < M:
                dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[5], dice[1], dice[4], dice[3], dice[0], dice[2]
                if arr[nx][ny] == 0:
                    arr[nx][ny] = dice[0]
                else:
                    dice[0] = arr[nx][ny]
                    arr[nx][ny] = 0
                print(dice[2])
                x = nx
                y = ny

        elif order == 2:
            nx = x + dx[order-1]
            ny = y + dy[order-1]
            if 0 <= nx < N and 0 <= ny < M:
                dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[1], dice[5], dice[3], dice[2], dice[0]
                if arr[nx][ny] == 0:
                    arr[nx][ny] = dice[0]
                else:
                    dice[0] = arr[nx][ny]
                    arr[nx][ny] = 0
                print(dice[2])
                x = nx
                y = ny

        elif order == 3:
            nx = x + dx[order-1]
            ny = y + dy[order-1]
            if 0 <= nx < N and 0 <= ny < M:
                dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[0], dice[1], dice[2], dice[4], dice[5]
                if arr[nx][ny] == 0:
                    arr[nx][ny] = dice[0]
                else:
                    dice[0] = arr[nx][ny]
                    arr[nx][ny] = 0
                print(dice[2])
                x = nx
                y = ny

        else:
            nx = x + dx[order-1]
            ny = y + dy[order-1]
            if 0 <= nx < N and 0 <= ny < M:
                dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[2], dice[3], dice[0], dice[4], dice[5]
                if arr[nx][ny] == 0:
                    arr[nx][ny] = dice[0]
                else:
                    dice[0] = arr[nx][ny]
                    arr[nx][ny] = 0
                print(dice[2])       
                x = nx
                y = ny     
        # print(x, y)
        # print(dice)
        # print(arr)