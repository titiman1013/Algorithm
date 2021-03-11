import sys; sys.stdin = open('9205.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    home = list(map(int, input().split()))
    stores = [list(map(int, input().split())) for _ in range(N)]
    target = list(map(int, input().split()))