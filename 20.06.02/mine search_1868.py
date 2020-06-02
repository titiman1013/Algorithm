import sys; sys.stdin = open('mine search.txt', 'r')
from collections import deque


dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def search(x, y, arr):
    pass



for tc in range(1, int(input())+1):
    N = int(input())
    arr = [input() for _ in range(N)]

    que = deque()

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '.':
                temp = 0
                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if arr[nx][ny] == '*':
                            temp += 1
                arr[i][j] = 'temp'

    print(arr)

    while True:
        pass