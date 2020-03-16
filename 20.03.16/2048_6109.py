import sys; sys.stdin = open('2048.txt', 'r')

for tc in range(1, int(input())+1):
    s = list(input().split())
    N = int(s[0])
    S = s[1]
    tile = [list(map(int, input().split())) for i in range(N)]
    ans = []

    if S == 'right':
        ans = f(N, tile)
    elif S == 'up':
        tile = cw(N, tile)
        ans = f(N, tile)
        for _ in range(3):
            ans = cw(N, ans)
    elif S == 'left':
        tile = cw(N, tile)
        tile = cw(N, tile)
        ans = f(N, tile)
        ans = cw(N, ans)
        ans = cw(N, ans)
    elif S == 'down':
        for _ in range(3):
            tile = cw(N, tile)
        ans = f(N, tile)
        ans = cw(N, ans)
        