import sys; sys.stdin = open('electronic bus.txt', 'r')


def go(now, gas, cnt):
    global res

    if cnt >= res:
        return

    if gas < 0:
        # print('m')
        return

    if now == len(arr):
        if cnt < res:
            res = cnt
            # print(now, gas, cnt)
            # print(visit)
        return
    
    # visit[now] = True
    go(now+1, arr[now-1]-1, cnt+1)
    
    # visit[now] = False
    go(now+1, gas-1, cnt)



for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    N = arr.pop(0)
    arr.append(0)

    # visit = [False] * N
    res = 10000000
    go(1, arr[0], 0)

    print(f'#{tc} {res}')