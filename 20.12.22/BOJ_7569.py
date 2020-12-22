import sys; sys.stdin = open('text1.txt', 'r')

for tc in range(1, int(input()) + 1):
    M, N, H = map(int, input().split())
    arr = [[list(map(int, input().split())) for i in range(N)] for j in range(H)]

    