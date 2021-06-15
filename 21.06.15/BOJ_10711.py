import sys; sys.stdin = open('10711.txt', 'r')

# time error

import sys

input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    H, W = map(int, input().split())
    board = [list(map(str, input())) for _ in range(H)]
