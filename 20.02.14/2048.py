import sys
sys.stdin = open("2048.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for t in range(T):
    N, S = input().split()
    N = int(N)
    arr = [[0]*(N+2)] + [[0] + list(map(int, input().split())) + [0] for i in range(N)] + [[0]*(N+2)]

    if S == 'up':
        for k in range(N-1):
            for i in range(1,N):
                for j in range(1,N+1):
                    if arr[i][j] == 0:
                        arr[i][j] = arr[i+1][j]
                        arr[i+1][j] = 0
        for p in range(1,N):
            for q in range(1,N+1):
                if arr[p][q] == 0:
                    arr[p][q] = arr[p+1][q]
                    arr[p+1][q] = 0
                    for i in range(1,N):
                        for j in range(1,N+1):
                            if arr[i][j] == 0:
                                arr[i][j] = arr[i+1][j]
                                arr[i+1][j] = 0
                if arr[p][q] == arr[p+1][q]:
                    arr[p][q] *= 2
                    arr[p+1][q] = 0
                    for i in range(1,N):
                        for j in range(1,N+1):
                            if arr[i][j] == 0:
                                arr[i][j] = arr[i+1][j]
                                arr[i+1][j] = 0

    if S == 'down':
        for k in range(N-1):
            for i in range(N,1,-1):
                for j in range(1,N+1):
                    if arr[i][j] == 0:
                        arr[i][j] = arr[i-1][j]
                        arr[i-1][j] = 0
        for p in range(N,1,-1):
            for q in range(1,N+1):
                if arr[p][q] == 0:
                    arr[p][q] = arr[p-1][q]
                    arr[p-1][q] = 0
                    for i in range(N,1,-1):
                        for j in range(1,N+1):
                            if arr[i][j] == 0:
                                arr[i][j] = arr[i-1][j]
                                arr[i-1][j] = 0
                if arr[p][q] == arr[p-1][q]:
                    arr[p][q] *= 2
                    arr[p-1][q] = 0
                    for i in range(N,1,-1):
                        for j in range(1,N+1):
                            if arr[i][j] == 0:
                                arr[i][j] = arr[i-1][j]
                                arr[i-1][j] = 0

    if S == 'left':
        for k in range(N-1):
            for i in range(1,N):
                for j in range(1,N+1):
                    if arr[j][i] == 0:
                        arr[j][i] = arr[j][i+1]
                        arr[j][i+1] = 0
        for p in range(1,N):
            for q in range(1,N+1):
                if arr[q][p] == 0:
                    arr[q][p] = arr[q][p+1]
                    arr[q][p+1] = 0
                    for i in range(1,N):
                        for j in range(1,N+1):
                            if arr[j][i] == 0:
                                arr[j][i] = arr[j][i+1]
                                arr[j][i+1] = 0
                if arr[q][p] == arr[q][p+1]:
                    arr[q][p] *= 2
                    arr[q][p+1] = 0
                    for i in range(1,N):
                        for j in range(1,N+1):
                            if arr[j][i] == 0:
                                arr[j][i] = arr[j][i+1]
                                arr[j][i+1] = 0

    if S == 'right':
        for k in range(N-1):
            for i in range(N,1,-1):
                for j in range(1,N+1):
                    if arr[j][i] == 0:
                        arr[j][i] = arr[j][i-1]
                        arr[j][i-1] = 0
        for p in range(N,1,-1):
            for q in range(1,N+1):
                if arr[q][p] == 0:
                    arr[q][p] = arr[q][p-1]
                    arr[q][p-1] = 0
                    for i in range(N,1,-1):
                        for j in range(1,N+1):
                            if arr[j][i] == 0:
                                arr[j][i] = arr[j][i-1]
                                arr[j][i-1] = 0
                if arr[q][p] == arr[q][p-1]:
                    arr[q][p] *= 2
                    arr[q][p-1] = 0
                    for i in range(N,1,-1):
                        for j in range(1,N+1):
                            if arr[j][i] == 0:
                                arr[j][i] = arr[j][i-1]
                                arr[j][i-1] = 0
    print('#{}'.format(t+1))
    for i in range(1,N+1):
        for j in range(1,N+1):
            print(arr[i][j],end=' ')
        print()