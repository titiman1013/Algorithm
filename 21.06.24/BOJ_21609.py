import sys; sys.stdin = open('21609.txt', 'r')

import sys


input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
