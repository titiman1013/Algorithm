import sys; sys.stdin = open('text1.txt', 'r')
from collections import deque
from copy import deepcopy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def melt():
    temp_list = deepcopy(arr)
    time = 0
    while True:
        time += 1
        for i in range(N):
            for j in range(N):
                if arr[i][j]:
                    temp = 0
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if 0 <= nx < N and 0 <= ny < N:
                            if arr[nx][ny] == 0:
                                temp += 1
                    temp_list[i][j] -= temp
        cnt = search_cnt(temp_list)
        if cnt == 0:
            return 0
        elif cnt == 2:
            return time
        # print(cnt)



def search_cnt(melt_list):
    temp_res = 0
    visited = deepcopy(melt_list)
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                temp_res += 1
                q = deque()
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N:
                            if visited[nx][ny]:
                                visited[nx][ny] = 0
                                q.append((nx, ny))
    
    return temp_res




for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    res = melt()
    print(res)