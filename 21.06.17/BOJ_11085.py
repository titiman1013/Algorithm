import sys; sys.stdin = open('11085.txt', 'r')

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



p, w = map(int, input().split())
c, v = map(int, input().split())
heap = []
for _ in range(w):
    start, end, width = map(int, input().split())
    heapq.heappush(heap, (-width, start, end))

parent = [i for i in range(p)]
rank = [1] * p

# # visited = [False] * p
# answer = 0
# # while not (visited[c] and visited[v]):
# while parent[c] != parent[v]:
#     width, start, end = heapq.heappop(heap)
#     # visited[start] = True
#     # visited[end] = True
#     if union(start, end):
#         answer = -width

answer = 0
while heap:
    width, start, end = heapq.heappop(heap)
    if union(start, end):
        if find(c) == find(v):
            answer = -width
            break

print(answer)