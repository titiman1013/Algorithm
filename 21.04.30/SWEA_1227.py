import sys; sys.stdin = open('1227.txt', 'r')

from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(maze, visited, start):
    global answer
    
    deq = deque([start])
    while deq:
        x, y = deq.popleft()
        visited[x][y] = 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 100 and 0 <= ny < 100:
                if maze[nx][ny] == '3':
                    answer = 1
                    return
                elif maze[nx][ny] == '0' and visited[nx][ny] == 0:
                    deq.append((nx, ny))
    return



for _ in range(10):
    tc = int(input())
    maze = list(input() for _ in range(100))
    answer = 0

    visited = list([0] * 100 for _ in range(100))
    bfs(maze, visited, [1, 1])

    print(f'#{tc} {answer}')