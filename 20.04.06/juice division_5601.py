import sys; sys.stdin = open("juice division.txt", "r")

for tc in range(1, int(input())+1):
    N = int(input())

    print(f'#{tc}', end=' ')
    for i in range(N):
        print('1/', end='')
        print(N, end=' ')
    print()    