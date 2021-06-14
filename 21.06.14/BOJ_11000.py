import sys; sys.stdin = open('11000.txt', 'r')

import sys, heapq

input = sys.stdin.readline

N = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(N)]

lectures.sort()

answer = 0
heap = []
for start, end in lectures:
    if (not heap or heap[0] > start):
        answer += 1
        heapq.heappush(heap, end)
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, end)

print(answer)