T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = []
    if N < M :
        for i in range(M-N+1):
            lis = []
            for j in range(N):
                lis.append(a[j]*b[i+j])
            result.append(sum(lis))
    elif N > M:
        for i in range(N-M+1):
            lis = []
            for j in range(M):
                lis.append(a[i+j]*b[j])
            result.append(sum(lis))
    else: # N = M
        for i in range(N):
            lis = []
            lis.append(a[i]*b[i])
            result.append(sum(lis))
    print(f'#{t+1} {max(result)}')
