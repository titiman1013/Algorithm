import sys; sys.stdin = open('1753.txt', 'r')

import sys

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]
