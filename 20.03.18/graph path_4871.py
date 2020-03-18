import sys; sys.stdin = open("graph path.txt", "r")

#
def dfs(V, start, end):
    visited = [0] * (V+1)
    stack = []
    stack.append(start)
    while stack:
        n = stack.pop()     # 방문할 노드를 스택에서 꺼냄
        visited[n] = 1      # 현재 위치 n에 방문 표시
        if n == end:
            return 1
        for t in adj[n]:    # n의 인접 노드중
            if visited[t] == 0:     # 방문안한 노드를 스택에 추가
                stack.append(t)
                n = t
    return 0




T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]      # 인접 리스트
    for _ in range(E):                  # 그래프 정보 저장
        n1, n2 = map(int, input().split())
        adj[n1].append(n2)              # 방향 그래프
    start, end = map(int, input().split())
    print('#{} {}'.format(tc, dfs(V, start, end)))

# #
# def dfs(n, end):
#     if n == end:        # 목적지면 1 반환
#         return 1
#     else:
#         visited[n] = 1
#         for t in adj[n]:
#             if visited[t] == 0:
#                 if dfs(t, end) == 1:
#                     return 1
#         return 0        # 목적지를 못찾은 경우



# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     adj = [[] for _ in range(V+1)]      # 인접 리스트
#     for _ in range(E):                  # 그래프 정보 저장
#         n1, n2 = map(int, input().split())
#         adj[n1].append(n2)              # 방향 그래프
#     start, end = map(int, input().split())
#     print('#{} {}'.format(tc, dfs(V, start, end)))
