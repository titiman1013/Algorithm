import sys; sys.stdin = open('12764.txt', 'r')

import sys

input = sys.stdin.readline

N = int(input())
people = [tuple(map(int, input().split())) for _ in range(N)]
