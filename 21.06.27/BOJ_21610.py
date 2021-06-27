import sys; sys.stdin = open('21610.txt', 'r')

import sys
dx, dy = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]


input = sys.stdin.readline

def move_cloud():
    for i in range(len(clouds)):
        x, y = clouds[i]
        clouds[i] = [(N + x + dx[dir - 1] * dis) % N, (N + y + dy[dir - 1] * dis) % N]
    return


def rain():
    for x, y in clouds:
        arr[x][y] += 1
        visited[x][y] = True
    return


def water_copy_bug():
    for x, y in clouds:
        cnt = 0
        for k in range(1, len(dx), 2):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny]:
                    cnt += 1
        arr[x][y] += cnt
    return


def make_cloud():
    tmp_cloud = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2:
                if visited[i][j] == False:
                    tmp_cloud.append([i, j])
                    arr[i][j] -= 2

    return tmp_cloud



for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    commands = [list(map(int, input().split())) for _ in range(M)]

    clouds = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]]
    for dir, dis in commands:
        move_cloud()
        visited = [[False] * N for _ in range(N)]
        rain()
        water_copy_bug()
        clouds = make_cloud()
    
    answer = 0
    for val in arr:
        answer += sum(val)
    print(answer)