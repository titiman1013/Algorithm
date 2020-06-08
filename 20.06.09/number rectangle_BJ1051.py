import sys; sys.stdin = open('number rectangle.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, list(input()))) for _ in range(N)]

    K = min(N, M)

    res = 0
    for i in range(N):
        for j in range(M):
            for k in range(0, K):
                if i + k < N and j + k < M:
                    if arr[i][j] == arr[i][j+k] == arr[i+k][j] == arr[i+k][j+k]:
                        if (k + 1) ** 2 > res:
                            res = (k + 1) ** 2
                            # print(i, j, k)
    
    print(f'#{tc} {res}')