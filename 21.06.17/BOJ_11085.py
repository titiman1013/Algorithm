import sys; sys.stdin = open('11085.txt', 'r')

import sys, heapq

input = sys.stdin.readline

p, w = map(int, input().split())
c, v = map(int, input().split())
heap = []
for _ in range(w):
    start, end, width = map(int, input().split())
    heapq.heappush(heap, (-width, start, end))