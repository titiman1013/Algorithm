import sys; sys.stdin = open('2252.txt', 'r')

#

# from collections import deque

# for tc in range(1, int(input()) + 1):
#     N, M = map(int, input().split())
#     infos = [tuple(map(int, input().split())) for _ in range(M)]

#     infos.sort()

#     parents = [[] for _ in range(N + 1)]
#     degrees = [1] * (N + 1)
#     for short, tall in infos:
#         # degrees[tall] = max(degrees[tall], degrees[short] + 1)
#         degrees[tall] += 1
#         parents[short].append(tall)

#     deq = deque()
#     for i in range(1, N + 1):
#         if degrees[i] == 1:
#             deq.append(i)

#     answer = []
#     while deq:
#         degree = deq.popleft()
#         for parent in parents[degree]:
#             degrees[parent] -= 1
#             if degrees[parent] == 1:
#                 deq.append(parent)

#         print(degree, end=' ')
#     print()




#

from collections import deque
import sys

input = sys.stdin.readline

def topo_sort():
    deq = deque()
    # res는 차수를 출력할 때 사용
    res = [0] * (n + 1)
    for i in range(1, n + 1):
        if degrees[i] == 0:
            deq.append(i)
            res[i] = 1

    while deq:
        now = deq.popleft()
        answer.append(now)
        for i in graph[now]:
            degrees[i] -= 1
            if degrees[i] == 0:
                deq.append(i)
                res[i] += res[now] + 1
    
    return answer



for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    degrees = [0] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        degrees[b] += 1
    
    answer = []
    answer = topo_sort()
    print(*answer)