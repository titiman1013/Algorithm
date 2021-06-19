import sys; sys.stdin = open('1766.txt', 'r')

import sys, heapq

input = sys.stdin.readline

def topo_sort():
    heap = []
    for i in range(1, N + 1):
        if degrees[i] == 0:
            heapq.heappush(heap, i)
    
    result = []
    while heap:
        now = heapq.heappop(heap)
        result.append(now)
        for i in graph[now]:
            degrees[i] -= 1
            if degrees[i] == 0:
                heapq.heappush(heap, i)
    
    return result



N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
degrees = [0] * (N + 1)
for _ in range(M):
    pre_problem, problem = map(int, input().split())
    graph[pre_problem].append(problem)
    degrees[problem] += 1

answer = topo_sort()
print(*answer)