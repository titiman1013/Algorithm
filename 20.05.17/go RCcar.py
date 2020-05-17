import sys; sys.stdin = open('go RCcar.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())

    res = 0
    velocity = 0
    for n in range(N):
        inputs = list(map(int, input().split()))
        state = inputs[0]
        if state == 0:
            pass
        elif state == 1:
            velocity += inputs[1]
        elif state == 2:
            velocity -= inputs[1]
            if velocity < 0:
                velocity = 0
        res += velocity
    print(f'#{tc} {res}')