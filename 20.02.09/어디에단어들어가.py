T = int(input())
for t in range(T):
    N,K = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    total  =0
    for i in range(N): # 가로판단
        n = 0
        cnt_temp = 0
        while n < N:
            if arr[i][n] == 1:
                cnt_temp += 1
                n += 1
            else:
                if cnt_temp == K:
                    total += 1
                n += 1
                cnt_temp = 0
        if cnt_temp == K:
            total += 1
 
    for i in range(N): # 세로판단
        n = 0
        cnt_temp = 0
        while n < N:
            if arr[n][i] == 1:
                cnt_temp += 1
                n += 1
            else:
                if cnt_temp == K:
                    total += 1
                n += 1
                cnt_temp = 0
        if cnt_temp == K:
            total += 1
    print(f'#{t+1} {total}')