import sys; sys.stdin = open('14567.txt', 'r')

import sys

input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    prerequisites = [tuple(map(int, input().split())) for _ in range(M)]
