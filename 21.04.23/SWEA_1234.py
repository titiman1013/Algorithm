import sys; sys.stdin = open('1234.txt', 'r')

for tc in range(1, 11):
    N, arr = map(str, input().split())
    arr = list(map(str, arr))