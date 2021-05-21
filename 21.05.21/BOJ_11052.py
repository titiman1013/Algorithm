import sys; sys.stdin = open('11052.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    cards = [0] + list(map(int, input().split()))