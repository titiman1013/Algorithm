import sys; sys.stdin = open('4615.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    plays = list(list(map(int, input().split())) for _ in range(M))