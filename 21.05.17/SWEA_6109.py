import sys; sys.stdin = open('6109.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, S = map(str, input().split())
    boards = list(list(map(int, input().split())) for _ in range(int(N)))