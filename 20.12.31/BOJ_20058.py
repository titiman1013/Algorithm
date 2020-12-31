import sys; sys.stdin = open('text1.txt', 'r')
from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def rotation(step):
    # 90도 회전 코드
    # arr = [*list(zip(*arr))]
    temp_arr = [[0] * (2 ** N) for _ in range(2 ** N)]

    for i in range(0, 2 ** N, step):
        for j in range(0, 2 ** N, step):
            for p in range(step):
                for q in range(step):
                    temp_arr[i + p][j + q] = arr[i + step - q - 1][j + p]
    
    return temp_arr


def magic():
    for i in range(2 ** N):
        for j in range(2 ** N):
            if arr[i][j]:
                temp = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < 2 ** N and 0 <= ny < 2 ** N:
                        if arr[nx][ny]:
                            temp += 1
                if temp < 3:
                    arr[i][j] -= 1


def sum_ice():
    sumVal = 0
    for i in range(2 ** N):
        sumVal += sum(arr[i])
    return sumVal


def bfs():
    visited = [[0] * (2 ** N) for _ in range(2 ** N)]
    max = -1

    for i in range(2 ** N):
        for j in range(2 ** N):
            if arr[i][j] and visited[i][j] == 0:
                temp = 1
                visited[i][j] = 1
                q = deque()
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < 2 ** N and 0 <= ny < 2 ** N:
                            if arr[nx][ny] and visited[nx][ny] == 0:
                                visited[nx][ny] = 1
                                temp += 1
                                q.append((nx, ny))
                if temp > max:
                    max = temp

    if max == -1:
        max = 0
    return max
    


for tc in range(1, int(input()) + 1):
    N, Q = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(2 ** N)]
    # 나눌 격자 크기
    L = list(map(int, input().split()))
    
    for idx in range(Q):
        arr = rotation(2 ** L[idx])
        magic()
        print(arr)
    res_sum = sum_ice()
    print(res_sum)
    res_cnt = bfs()
    print(res_cnt)
    print('--------------------------------')