import sys; sys.stdin = open('15685.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    curves = [list(map(int, input().split())) for _ in range(N)]