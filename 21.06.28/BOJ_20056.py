import sys; sys.stdin = open('20056.txt', 'r')

import sys


input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    fireball_infos = [list(map(int, input().split())) for _ in range(M)]
