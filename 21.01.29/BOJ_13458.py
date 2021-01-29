import sys; sys.stdin = open('text1.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    A = list(map(int, input().split()))
    B, C = map(int, input().split())