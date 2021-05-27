import sys; sys.stdin = open('1916.txt', 'r')

import sys, heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
infos = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
start, end = map(int, sys.stdin.readline().split())

nodes = dict()
for info in infos:
    nodes[info[0]] = nodes.get(info[0], []) + [(info[1], info[2])]

distance = {i: float('inf') if i != start else 0 for i in range(1, N + 1)}
heap = []
heapq.heappush(heap, start)
while heap:
    current_node = heapq.heappop(heap)
    if nodes.get(current_node):
        for next_node, dis in nodes[current_node]:
            if distance[next_node] > distance[current_node] + dis:
                distance[next_node] = distance[current_node] + dis
                heapq.heappush(heap, next_node)

print(distance.get(end))