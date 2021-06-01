import sys; sys.stdin = open('1774.txt', 'r')

# Prim collect

# from collections import defaultdict
# import sys, heapq

# input = sys.stdin.readline

# N, M = map(int, input().split())
# points = defaultdict(tuple)
# num = 0
# for _ in range(N):
#     num += 1
#     x, y = map(int, input().split())
#     points[num] = (x, y)
# connects = list(tuple(map(int, input().split())) for _ in range(M))

# adj = defaultdict(list)
# for s in range(1, N + 1):
#     for e in range(1, N + 1):
#         if s != e:
#             s_x, s_y = points.get(s)
#             e_x, e_y = points.get(e)
#             adj[s].append((e, (abs(s_x - e_x) ** 2 + abs(s_y - e_y) ** 2) ** 0.5))

# for x, y in connects:
#     adj[x].append((y, 0))
#     adj[y].append((x, 0))

# visited = [0] * (N + 1)
# edge_list = []

# res = 0
# visited[1] = 0
# heapq.heappush(edge_list, (0, 1))
# while edge_list:
#     min_cost, current_node = heapq.heappop(edge_list)
#     if visited[current_node]: continue
#     visited[current_node] = 1
#     res += min_cost
#     for next_node, cost in adj[current_node]:
#         if visited[next_node] == 0:
#             heapq.heappush(edge_list, (cost, next_node))

# print(f'{res:.2f}')




# Prim faster

# import heapq

# N, M = map(int, input().split())

# node = [list(map(int, input().split())) for _ in range(N)]
# visited = [False] * N
# graph = [[0] * N for _ in range(N)]

# for i in range(N):
#     for j in range(i+1, N):
#         dis = (node[i][0] - node[j][0]) ** 2 + (node[i][1] - node[j][1]) ** 2
#         dis = dis ** 0.5
#         graph[i][j] = dis
#         graph[j][i] = dis

# for i in range(M):
#     a, b = map(int, input().split())
#     graph[a - 1][b - 1] = 0
#     graph[b - 1][a - 1] = 0


# heap = [[0, 0]]
# answer = 0
# for i in range(N):
#     while heap:
#         cost, idx = heapq.heappop(heap)
#         if visited[idx]:
#             continue
#         for i in range(N):
#             if not visited[i]:
#                 heapq.heappush(heap, [graph[idx][i], i])
#         visited[idx] = True
#         answer += cost
#         break

# print(f'{answer:.2f}')




# Kruskal

import sys, heapq

input = sys.stdin.readline

def find(x):
    if parent[x] == x: return x

    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x, y = find(x), find(y)

    if x == y: return False

    if rank[x] < rank[y]:
        x, y = y, x

    parent[y] = x

    if rank[x] == rank[y]:
        rank[x] += 1
    return True



N, M = map(int, input().split())
points = [0] + [list(map(int, input().split())) for _ in range(N)]
parent = [i for i in range(N + 1)]
rank = [1] * (N + 1)
for _ in range(M):
    union(*map(int, input().split()))

heap = []
for i in range(1, N):
    for j in range(i + 1, N + 1):
        dis = (abs(points[i][0] - points[j][0]) ** 2 + abs(points[i][1] - points[j][1]) ** 2) ** 0.5
        heapq.heappush(heap, (dis, i, j))

answer = 0
while heap:
    cost, start, end = heapq.heappop(heap)

    if union(start, end):
        answer += cost

print(f'{answer:.2f}')