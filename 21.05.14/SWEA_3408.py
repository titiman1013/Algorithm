import sys; sys.stdin = open('3408.txt', 'r')

# time exceed

def calc(N, num):
    if num == 1:
        res = 0
        for i in range(1, N + 1):
            res += i
        return res

    elif num == 2:
        res = 0
        for i in range(1, N * 2, 2):
            res += i
        return res
    elif num == 3:
        res = 0
        for i in range(2, N * 2 + 1, 2):
            res += i
        return res



for tc in range(1, int(input()) + 1):
    N = int(input())

    S1, S2, S3 = calc(N, 1), calc(N, 2), calc(N, 3)

    print(f'#{tc} {S1} {S2} {S3}')