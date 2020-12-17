import sys; sys.stdin =  open('text1.txt', 'r')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def search_shark():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                return [i, j]


def search_fish(x, y):
    # 방문확인, 걸리는 시간
    visited = [[[0, 0] for _ in range(N)] for _ in range(N)]
    visited[x][y][1] = time
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        temp_move = []
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny][0] == 0:
                    visited[nx][ny][0] = 1
                    visited[nx][ny][1] = visited[x][y][1] + 1
                    if arr[nx][ny] < shark_size:
                        if arr[nx][ny]:
                            temp_move.append([nx, ny])
                            arr[nx][ny] = 0
                            continue
                    else:
                        q.append([nx, ny])
        print(temp_move)
        if temp_move:
            distance = 0
            pos = []
            for i in range(len(temp_move)):
                temp = abs(x - temp_move[i][0]) + abs(y - temp_move[i][1])
                if pos:
                    if temp < distance:
                        distance = temp
                        pos = [temp_move[i][0], temp_move[i][1]]
                    elif temp == distance:
                        if temp_move[i][0] < pos[0]:
                            pos = [temp_move[i][0], temp_move[i][1]]
                        elif temp_move[i][0] == pos[0]:
                            if temp_move[i][1] < pos[1]:
                                pos = [temp_move[i][0], temp_move[i][1]]
                else:
                    distance = temp
                    pos = [temp_move[i][0], temp_move[i][1]]
            return pos
    return False



for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int ,input().split())) for _ in range(N)]

    # 초기 아기상어 크기는 2 
    # 1초에 상하좌우 인접칸으로 한 칸 이동
    # 크기가 더 작은 물고기만 먹을 수 있고, 같으면 지나갈 수 있다
    # 거리가 가장 가까운 물고기를 먹으러 간다
    #   - 거리가 가까운 물고기 > 위에 있는 물고기 > 왼쪽 물고기
    # 더이상 먹을 수 없으면 종료
    # 9가 아기상어 위치

    shark_size = 2
    time = 0
    shark_pos = search_shark()
    while True:
        move_point = search_fish(shark_pos[0], shark_pos[1])
        if move_point == False:
            print(f'#{tc} {time}')
            break
