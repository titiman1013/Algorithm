import sys; sys.stdin = open('11315.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [input() for _ in range(N)]