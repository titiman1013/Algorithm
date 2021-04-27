import sys; sys.stdin = open('5603.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    dummys = list(int(input()) for _ in range(N))
    answer = 0

    avg = sum(dummys) // N
    tmp = 0
    for dummy in dummys:
        tmp += abs(dummy - avg)
    answer = tmp // 2

    print(f'#{tc} {answer}')