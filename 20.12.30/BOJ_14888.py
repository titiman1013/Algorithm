import sys; sys.stdin = open('text1.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    operator = list(map(int, input().split()))