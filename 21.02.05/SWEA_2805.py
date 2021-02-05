import sys; sys.stdin = open('2805.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]