import sys; sys.stdin = open('1774.txt', 'r')

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
points = defaultdict(tuple)
num = 0
for _ in range(N):
    num += 1
    x, y = map(int, input().split())
    points[num] = (x, y)
connects = list(tuple(map(int, input().split())) for _ in range(M))
