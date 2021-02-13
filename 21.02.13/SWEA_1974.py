import sys; sys.stdin = open('1974.txt', 'r')

for tc in range(1, int(input()) + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]