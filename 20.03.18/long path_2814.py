import sys; sys.stdin = open("long path.txt", "r")

# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     # N개의 정점 M개의 간선
#     gansun = [list(map(int, input().split())) for _ in range(M)]
    
#     stack = []
#     for k in range(M):
#         for i in range(M):
            

# 재귀
def f(n, k, c):     # n 방문노드, k 전체노드, c 경로에 포함된 노드 개수(n 미포함)
    global maxV
    if maxV < c + 1:    # n을 포함한 경로의 길이가 더 길면
        maxV = c + 1    # 갱신
    visited[n] = 1      # 현재 경로에서 재진입 방지
    for i in range(1, k+1):     # 모든 노드 i에 대해
        if adj[n][i] == 1 and visited[i] == 0:  # n에 인접이고 방문하지 않은 곳이면
            f(i, k, c+1)
    visited[n] = 0      # 다른 경로에서 n으로 진입 허용
    


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    adj = [[0] * (N+1) for _ in range(N+1)]
    visited = [0] * (N+1)
    maxV = 0
    for _ in range(M):
        n1, n2 = map(int, input().split())
        adj[n1][n2] = 1
        adj[n2][n1] = 1
    for i in range(1, N+1):     # 각 노드에서 출발해본다.
        f(i, N, 0)  # 방문노드, 전체노드, 경로에 포함된 노드
    print('#{} {}'.format(tc, maxV))