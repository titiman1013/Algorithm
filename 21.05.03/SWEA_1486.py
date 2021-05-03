import sys; sys.stdin = open('1486.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))