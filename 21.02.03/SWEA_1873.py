import sys; sys.stdin = open('1873.txt', 'r')

for tc in range(1, int(input()) + 1):
    H, W = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(H)]
    N = int(input())
    commands = input()