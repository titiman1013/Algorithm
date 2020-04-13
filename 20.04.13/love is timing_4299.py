import sys; sys.stdin = open("love is timing.txt", "r")

for tc in range(1, int(input())+1):
    D, H, M = map(int, input().split())

    res = (D - 11) * 24 * 60 + (H - 11) * 60 + (M - 11)
    if res < 0:
        res = -1
    print(f'#{tc} {res}')