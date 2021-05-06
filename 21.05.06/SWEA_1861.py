import sys; sys.stdin = open('1861.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))