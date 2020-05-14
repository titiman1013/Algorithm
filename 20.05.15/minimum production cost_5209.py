import sys; sys.stdin = open('minimum production cost.txt', 'r')

def select(i, j, temp):
    global res

    if j == N:
        select(i+1, 0, temp)
    
    else:
        select(i, j+1, temp+arr[i][j])



for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    success = [0] * N
    res = 0
    for i in range(N):
        temp = 100
        factory = 0
        for j in range(N):
            if success[j] == 1:
                continue
            if arr[i][j] < temp:
                temp = arr[i][j]
                factory = j
        success[factory] = 1
        res += temp

    print(f'#{tc} {res}')