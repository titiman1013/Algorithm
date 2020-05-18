import sys; sys.stdin = open('usb mystery.txt', 'r')

for tc in range(1, int(input())+1):
    p, q = map(float, input().split())
    # p: 처음꽂을때 올바른 면으로 꽂을 확률
    # q: 올바른 면으로 꽂았을 때 정상적으로 꽂힐 확률

    print(f'#{tc}', end=' ')
    if (1 - p) * q < p * (1 - q) * q:
        print('YES')
    else:
        print('NO')