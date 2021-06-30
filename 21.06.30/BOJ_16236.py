import sys; sys.stdin = open('16236.txt', 'r')

import sys
from collections import deque


input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def search_fish():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                shark_pos = (i, j)

    fishes_pos = []
    time_table = [[0] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    deq = deque([shark_pos])
    visited[shark_pos[0]][shark_pos[1]] = True
    while deq:
        x, y = deq.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
                if arr[nx][ny] <= shark_size:
                    time_table[nx][ny] = time_table[x][y] + 1
                    deq.append((nx, ny))
                    visited[nx][ny] = True

                if arr[nx][ny] and arr[nx][ny] < shark_size:
                    fishes_pos.append((time_table[nx][ny], nx, ny))
                
                
    return sorted(fishes_pos)[0] if fishes_pos else False, shark_pos


def move_shark(selected_fish, shark_pos):
    global total_time, shark_size, eat_cnt

    move_time, fish_x, fish_y = selected_fish
    total_time += move_time

    arr[fish_x][fish_y] = 9
    arr[shark_pos[0]][shark_pos[1]] = 0

    eat_cnt += 1
    if eat_cnt == shark_size:
        shark_size += 1
        eat_cnt = 0
    
    return



for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    shark_size = 2
    eat_cnt = 0
    total_time = 0
    while True:
        searched_fish, shark_pos = search_fish()
        if searched_fish == False:
            break
        move_shark(searched_fish, shark_pos)

    answer = total_time
    print(answer)