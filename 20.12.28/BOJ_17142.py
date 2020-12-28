import sys; sys.stdin = open('text1.txt', 'r')
from collections import deque
from itertools import combinations


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def virus_diffusion(select_virus):
    time_list = [[-1] * N for _ in range(N)]
    q = deque()
    for i in range(len(select_virus)):
        time_list[select_virus[i][0]][select_virus[i][1]] = 0
        q.append(select_virus[i])

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                # arr[nx][ny] == 0 으로 설정하면 비활성바이러스가 활성바이러스로 변하는 것을 찾아줄 수 없음
                if arr[nx][ny] != 1 and time_list[nx][ny] == -1:
                    time_list[nx][ny] = time_list[x][y] + 1
                    q.append((nx, ny))
    
    # gas diffusion check & result
    max_time = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                if time_list[i][j] > max_time:
                    max_time = time_list[i][j]
                elif time_list[i][j] == -1:
                    return 100000000
    return max_time



for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # virus combinations
    virus = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                virus.append((i, j))
    virus_comb = list(combinations(virus, M))
    
    # minimum time check
    time = 100000001
    for virus_list in virus_comb:
        temp = virus_diffusion(virus_list)
        if temp < time:
            time = temp

    if time == 100000000:
        time = -1
    
    print(time)
    # print(f'{tc} {time}')