import sys; sys.stdin = open('1774.txt', 'r')

from collections import defaultdict
import sys, heapq

input = sys.stdin.readline

N, M = map(int, input().split())
points = defaultdict(tuple)
num = 0
for _ in range(N):
    num += 1
    x, y = map(int, input().split())
    points[num] = (x, y)
connects = list(tuple(map(int, input().split())) for _ in range(M))

adj = defaultdict(list)
for s in range(1, N + 1):
    for e in range(1, N + 1):
        if s != e:
            s_x, s_y = points.get(s)
            e_x, e_y = points.get(e)
            adj[s].append((e, (abs(s_x - e_x) ** 2 + abs(s_y - e_y) ** 2) ** 0.5))

for x, y in connects:
    adj[x].append((y, 0))
    adj[y].append((x, 0))

visited = [0] * (N + 1)
edge_list = []

res = 0
visited[1] = 0
heapq.heappush(edge_list, (0, 1))
while edge_list:
    min_cost, current_node = heapq.heappop(edge_list)
    if visited[current_node]: continue
    visited[current_node] = 1
    res += min_cost
    for next_node, cost in adj[current_node]:
        if visited[next_node] == 0:
            heapq.heappush(edge_list, (cost, next_node))

print(f'{res:.2f}')