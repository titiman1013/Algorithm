import sys; sys.stdin = open('5603.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    dummys = list(int(input()) for _ in range(N))
    answer = 0