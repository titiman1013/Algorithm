import sys; sys.stdin = open('minimum production cost.txt', 'r')

def select(cnt, total):
    global res
    if res < total:
        return

    if sum(success) == N:
        if total < res:
            res = total
        return

    for i in range(N):
        if success[i] == 0:
            success[i] = 1
            select(cnt+1, total+arr[cnt][i])
            success[i] = 0

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    success = [0] * N
    res = 1000000000
    select(0, 0)

    print(f'#{tc} {res}')