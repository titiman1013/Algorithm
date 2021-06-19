import sys; sys.stdin = open('1766.txt', 'r')

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
for _ in range(M):
    pre_problem, problem = map(int, input().split())