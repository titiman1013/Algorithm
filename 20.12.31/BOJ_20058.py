import sys; sys.stdin = open('text1.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, Q = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(2 ** N)]
    magic_lst = list(map(int, input().split()))