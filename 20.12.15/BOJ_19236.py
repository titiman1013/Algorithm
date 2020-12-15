import sys; sys.stdin = open('text1.txt', 'r')

for tc in range(1, int(input()) + 1):
    # ai, bi: 물고기번호, 방향
    arr = [list(map(int, input().split())) for _ in range(4)]
    