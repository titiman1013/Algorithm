import sys; sys.stdin = open("forest of strange horn.txt", "r")

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    x = M
    y = 0
    while True:
        if x + y * 2 == N:
            break
        else:
            x -= 1
            y += 1

    print(f'#{tc} {x} {y}')