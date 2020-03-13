import sys; sys.stdin = open('russia flag.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split()) 
    arr = list(input() for _ in range(N)) 
    #0~i, i+1~j, j+1~N-1
    w = [0] * N
    b = [0] * N
    r = [0] * N
    for i in range(N):
        w[i] = arr[i].count("W")
        b[i] = arr[i].count("B")
        r[i] = M - w[i] - b[i]
 
    for i in range(1, N):
        w[i] += w[i - 1] # 왜 하나씩 빼주지???
        b[i] += b[i - 1]
        r[i] += r[i - 1]
 
    ans = N * M
    for i in range(0, N-3+1):
        for j in range(i+1, N-2+1):
            # 흰색이 아닌 칸수 = 전체 칸수 - 흰색 수
            cnt = M * (i+1) - w[i]
            cnt += M * (j - i) - (b[j] - b[i])
            cnt += M * (N - 1 - (j + 1 - 1)) - (r[N-1] - r[j])
            ans = min(ans, cnt)
    print('#%d %d' % (tc, ans))
