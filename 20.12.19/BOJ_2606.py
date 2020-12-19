import sys; sys.stdin = open('text1.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    M = int(input())
    arr = [list(map(int, input().split())) for _ in range(M)]