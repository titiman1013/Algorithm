import sys; sys.stdin = open('11000.txt', 'r')

import sys

input = sys.stdin.readline

N = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(N)]
