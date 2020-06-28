import sys; sys.stdin = open('most long way.txt', 'r')

def dfs(current_node, value):
    global max_result
 
    if max_result < value:
        max_result = value
    for next_node in range(1, N + 1):
        if nodes[current_node][next_node] and not visited[next_node]:
            visited[next_node] = 1
            dfs(next_node, value + 1)
            visited[next_node] = 0
 
 
for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    links = [list(map(int, input().split())) for _ in range(M)]
 
    if len(links) == 0:
        print('#{} {}'.format(t, 1))
 
    else:
        nodes = [[0] * (N + 1) for _ in range(N + 1)]
        for start, end in links:
            nodes[start][end], nodes[end][start] = 1, 1
 
        max_result = 1
        for index in range(1, N + 1):
            visited = [0] * (N + 1)
            visited[index] = 1
            dfs(index, 1)
        print('#{} {}'.format(t, max_result))