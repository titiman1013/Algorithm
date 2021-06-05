import sys; sys.stdin = open('1915.txt', 'r')

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
