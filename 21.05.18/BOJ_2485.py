import sys; sys.stdin = open('2485.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    trees = list(int(input()) for _ in range(N))