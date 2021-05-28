import sys; sys.stdin = open('1107.txt', 'r')

import sys

for tc in range(1, int(input()) + 1):
    input = sys.stdin.readline
    N = int(input())
    M = int(input())
    if M > 0:
        errors = list(map(int, input().split()))
    else:
        errors = []