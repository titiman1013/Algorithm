import sys; sys.stdin = open('19598.txt', 'r')

# time exceed

import sys, heapq

input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    N = int(input())
    conferences = [tuple(map(int, input().split())) for _ in range(N)]

    conferences = sorted(conferences, key=lambda x : x[0])

    answer = 0
    heap = []
    for start, end in conferences:
        if heap:
            if min(heap) <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
            if len(heap) > answer:
                answer = len(heap)
        else:
            heapq.heappush(heap, end)

    print(answer)