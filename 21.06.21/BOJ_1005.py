import sys; sys.stdin = open('1005.txt', 'r')

import sys

input = sys.stdin.readline

for _ in range(1, int(input()) + 1):
    for tc in range(1, int(input()) + 1):
        N, K = map(int, input().split())
        times = [0] + list(map(int, input().split()))
        orders = [tuple(map(int, input().split())) for _ in range(K)]
        target = int(input())