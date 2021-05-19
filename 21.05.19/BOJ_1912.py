import sys; sys.stdin = open('1912.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    nums = list(map(int, input().split()))