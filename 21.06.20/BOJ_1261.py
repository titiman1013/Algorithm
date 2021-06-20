import sys; sys.stdin = open('1261.txt', 'r')

import sys

input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    M, N = map(int, input().split())
    maze = [list(map(int, input().strip())) for _ in range(N)]
