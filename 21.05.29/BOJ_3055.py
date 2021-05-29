import sys; sys.stdin = open('3055.txt', 'r')

import sys

input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    R, C = map(int, input().split())
    arr = [list(map(str, input()))[:C] for _ in range(R)]
    