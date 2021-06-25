import sys; sys.stdin = open('16724.txt', 'r')

import sys


input = sys.stdin.readline

N, M = map(int, input().split())
board = list(input().rstrip('\n') for _ in range(N))
