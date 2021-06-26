import sys; sys.stdin = open('21608.txt', 'r')

import sys


input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    N = int(input())
    students = [list(map(int, input().split())) for _ in range(N ** 2)]
