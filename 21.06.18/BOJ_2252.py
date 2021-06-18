import sys; sys.stdin = open('2252.txt', 'r')

from collections import deque

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    infos = [tuple(map(int, input().split())) for _ in range(M)]

    infos.sort()

    parents = [[] for _ in range(N + 1)]
    degrees = [1] * (N + 1)
    for short, tall in infos:
        # degrees[tall] = max(degrees[tall], degrees[short] + 1)
        degrees[tall] += 1
        parents[short].append(tall)

    deq = deque()
    for i in range(1, N + 1):
        if degrees[i] == 1:
            deq.append(i)

    answer = []
    while deq:
        degree = deq.popleft()
        for parent in parents[degree]:
            degrees[parent] -= 1
            if degrees[parent] == 1:
                deq.append(parent)

        print(degree, end=' ')
    print()