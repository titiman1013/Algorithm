import sys; sys.stdin = open('1249.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(list(map(int, input())) for _ in range(N))