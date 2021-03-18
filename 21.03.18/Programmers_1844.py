from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(maps, m, n, pos, target):
    move_cnt = [[0] * m for _ in range(n)]
    move_cnt[pos[0]][pos[1]] = 1
    deq = deque([pos])
    while deq:
        x, y = deq.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] and move_cnt[nx][ny] == 0:
                    if nx == target[0] and ny == target[1]:
                        return move_cnt[x][y] + 1
                    deq.append((nx, ny))
                    move_cnt[nx][ny] = move_cnt[x][y] + 1
    return -1


def solution(maps):
    answer = 0

    n, m = len(maps), len(maps[0])
    start = [0, 0]
    end = [n - 1, m - 1]
    answer = bfs(maps, m, n, start, end)

    return answer




print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))

# answer
# 11
# -1