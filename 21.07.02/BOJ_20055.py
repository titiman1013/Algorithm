import sys; sys.stdin = open('20055.txt', 'r')

import sys


input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    durability = list(map(int, input().split()))
