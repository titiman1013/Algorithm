import sys; sys.stdin = open('1940.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    commands = [list(map(int, input().split())) for _ in range(N)]