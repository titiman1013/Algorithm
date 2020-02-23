G = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [3, 6]]
visited = [0] * 8

# DFS

def dfs(v):
    stack = []
    stack.append(v)
    while stack:
        v = stack.pop(-1)
        if not visited[v]:
            visited[v] = 1
            print(v, end=' ')
            for w in G[v]:
                if not visited[w]:
                    stack.append(w)


def dfsr(v):
    visited[v] = 1
    print(v, end=' ')
    for w in G[v]:
        if not visited[w]:
            dfsr(w)



# BFS

def bfs(v):
    que = []
    que.append(v)
    while que:
        v = que.pop(0)
        if not visited[v]:
            visited[v] = 1
            print(v, end=' ')
            for w in G[v]:
                if not visited[w]:
                    que.append(w)

                
