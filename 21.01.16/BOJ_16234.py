import sys; sys.stdin = open('text1.txt', 'r')

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def check(clone):
    pass



for tc in range(1, int(input()) + 1):
    N, L, R = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    res = check(arr)
    print(res)