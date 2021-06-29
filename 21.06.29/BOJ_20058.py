import sys; sys.stdin = open('20058.txt', 'r')


import sys


input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    N, Q = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(2 ** N)]
    spells = list(map(int, input().split()))