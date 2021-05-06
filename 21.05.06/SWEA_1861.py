import sys; sys.stdin = open('1861.txt', 'r')

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def search(start):
    global N

    cnt = 0
    stack = [start]
    while stack:
        x, y = stack.pop()
        cnt += 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[x][y] + 1 == arr[nx][ny]:
                    stack.append((nx, ny))
    return cnt



for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))
    answer = [float('inf'), 0]

    for i in range(N):
        for j in range(N):
            cnt = search((i, j))
            if cnt > answer[1]:
                answer[1] = cnt
                answer[0] = arr[i][j]
            elif cnt == answer[1]:
                if arr[i][j] < answer[0]:
                    answer[0] = arr[i][j]

    print(f'#{tc} {answer[0]} {answer[1]}')