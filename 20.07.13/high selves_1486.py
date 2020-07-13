import sys; sys.stdin = open('high selves.txt', 'r')

def select(cnt):
    global res
    if cnt == N:
        temp = 0
        for i in range(N):
            if check[i]:
                temp += arr[i]
        if temp >= B and abs(temp - B) < res:
            res = abs(temp - B)
            # print(check)
        return

    check[cnt] = True
    select(cnt+1)
    check[cnt] = False
    select(cnt+1)



for tc in range(1, int(input())+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    check = [0] * N
    res = 100000
    select(0)

    print(f'#{tc} {res}')