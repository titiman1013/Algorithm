import sys; sys.stdin = open('1753.txt', 'r')

import sys
import heapq
from collections import defaultdict

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]

nodes = defaultdict(list)
for line in lines:
    nodes[line[0]].append((line[1], line[2]))

distance = {i: float('inf') if i != K else 0 for i in range(1, V + 1)}
heap = []
heapq.heappush(heap, (0, K))
while heap:
    current_dis, current_node = heapq.heappop(heap)
    # if distance[current_node] < current_dis: continue
    for next_node, dis in nodes[current_node]:
        if distance[next_node] > distance[current_node] + dis:
            distance[next_node] = distance[current_node] + dis
            heapq.heappush(heap, (distance[next_node], next_node))

for val in distance.values():
    if val == float('inf'):
        print('INF')
    else:
        print(val)