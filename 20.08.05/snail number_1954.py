import sys; sys.stdin = open('snail number.txt', 'r')

move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    direction = 0

    i, j = 0, 0
    num = 1
    while num < N ** 2 + 1:
        arr[i][j] = num
        visited[i][j] = 1
        dx, dy = move[direction]
        nx, ny = i + dx, j + dy
        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny]:
                direction += 1
        else:
            direction += 1
        
        if direction == 4:
            direction = 0

        i, j = i + move[direction][0], j + move[direction][1]
        num += 1
    
    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()