import sys; sys.stdin = open('text1.txt', 'r')
from collections import deque

# 두 정점 사이에 여러 개의 간선이 있을 수 있다고 해서 +1식으로 계산해주었는데
# 어차피 한 번 들렀던 곳은 추가해주지 않으니 -1 계산보다는 0으로 바꿔주는것이 옳다
# -1식으로 계산하면 dfs에서는 들렀던 곳을 다시 들릴 수 있는 불상사가 발생

def dfs():
    graph = [[0] * N for _ in range(N)]
    for i in range(M):
        x, y = arr[i]
        graph[x - 1][y - 1] += 1
        graph[y - 1][x - 1] += 1

    result = [V]
    stack = [V - 1]
    
    while stack:
        x = stack.pop()
        if x + 1 not in result:
            result.append(x + 1)
        for k in range(N - 1, -1, -1):
            if graph[x][k] >= 1:
                graph[x][k] = 0
                graph[k][x] = 0
                stack.append(k)
    
    return result


def bfs():
    graph = [[0] * N for _ in range(N)]
    for i in range(M):
        x, y = arr[i]
        graph[x - 1][y - 1] += 1
        graph[y - 1][x - 1] += 1

    result = [V]
    q = deque()
    q.append(V - 1)

    while q:
        x = q.popleft()
        if x + 1 not in result:
            result.append(x + 1)
        for k in range(N):
            if graph[x][k] >= 1:
                # 여기는 -1 로 계산해도 상관이 없음
                # 너비우선은 확산형식이라 출력 순서에 영향을 미치지 않음
                graph[x][k] = 0
                graph[k][x] = 0
                q.append(k)
    
    return result



for tc in range(1, int(input()) + 1):
    N, M, V = map(int, input().split())
    arr = [list(map(int ,input().split())) for _ in range(M)]

    dfs_res = dfs()
    for i in range(len(dfs_res)):
        print(dfs_res[i], end=" ")
    print()
    bfs_res = bfs()
    for i in range(len(bfs_res)):
        print(bfs_res[i], end=" ")
    print()