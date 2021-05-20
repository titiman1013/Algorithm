import sys; sys.stdin = open('2293.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    coins = list(int(input()) for _ in range(N))