import sys; sys.stdin = open('container delivery.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    res = 0
    for i in range(len(trucks)):
        temp = 0
        for j in range(len(containers)):
            if containers[j] <= trucks[i] and containers[j] > temp:
                temp = containers[j]
        print(temp)
        if temp:
            containers.remove(temp)
        res += temp

    print(f'#{tc} {res}')