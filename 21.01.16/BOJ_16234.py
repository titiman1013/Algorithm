import sys; sys.stdin = open('text1.txt', 'r')
from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def check(clone):
    res = 0
    while True:
        flag = 0
        visited = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 0:
                    visited[i][j] = 1
                    deq = deque()
                    deq.append((i, j))
                    union = [(i, j)]
                    while deq:
                        x, y = deq.popleft()
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                                if L <= abs(clone[x][y] - clone[nx][ny]) <= R:
                                    union.append((nx, ny))
                                    deq.append((nx, ny))
                                    visited[nx][ny] = 1
                    if len(union) > 1:
                        flag = 1
                        people = sum(clone[x][y] for x, y in union) // len(union)
                        for x, y in union:
                            clone[x][y] = people
        if flag == 0: break
        res += 1
    return res



for tc in range(1, int(input()) + 1):
    N, L, R = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    res = check(arr)
    print(res)