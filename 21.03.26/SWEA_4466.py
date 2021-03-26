import sys; sys.stdin = open('4466.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    score = list(map(int, input().split()))
    