import sys; sys.stdin = open('text1.txt', 'r')
from collections import deque

def bfs():
    deq = deque()
    deq.append(1)
    while deq:
        x = deq.popleft()
        for i in range(2, N + 1):
            if arr[x][i] and parent[i] == 0:
                deq.append(i)
                parent[i] = x



for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(N - 1):
        x, y = map(int, input().split())
        arr[x][y] = 1
        arr[y][x] = 1
    parent = [0] * (N + 1)

    bfs()
    for i in range(2, len(parent)):
        print(parent[i])