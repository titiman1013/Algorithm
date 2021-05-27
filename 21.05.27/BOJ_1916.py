import sys; sys.stdin = open('1916.txt', 'r')

import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
infos = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
start, end = map(int, sys.stdin.readline().split())
