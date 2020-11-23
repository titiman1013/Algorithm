import sys; sys.stdin = open('text.txt', 'r')

for tc in range(3):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    
    res = 0
    flag = 0
    for i in range(len(arr)):
        if flag == 1: break
        for j in range(len(arr)):
            if flag == 1: break
            if i == j: continue;
            for k in range(len(arr)):
                if flag == 1: break
                if k == i or k == j: continue;
                else:
                    temp = arr[i] + arr[j] + arr[k]
                    if res < temp < M:
                        res = temp
                    elif temp == M:
                        res = temp
                        flag = 1
                        break
    print(f'{tc + 1} {res}')