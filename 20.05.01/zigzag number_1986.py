import sys; sys.stdin = open('zigzag number.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())

    res = 0
    for i in range(1, N+1):
        if i % 2:
            res += i
        else:
            res -= i

    print(f'#{tc} {res}')