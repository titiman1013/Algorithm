import sys; sys.stdin = open('2819.txt', 'r')

for tc in range(1, int(input()) + 1):
    arr = list(list(map(str, input().split())) for _ in range(4))