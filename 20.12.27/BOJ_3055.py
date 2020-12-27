import sys; sys.stdin = open('text1.txt', 'r')

for tc in range(1, int(input()) + 1):
    R, C = map(int, input().split())
    arr = [input() for _ in range(R)]