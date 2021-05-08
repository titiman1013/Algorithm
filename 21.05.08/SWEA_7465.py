import sys; sys.stdin = open('7465.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(M))