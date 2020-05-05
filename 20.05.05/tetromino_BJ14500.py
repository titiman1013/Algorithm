import sys; sys.stdin = open('tetromino.txt', 'r')

A = [[[1, 0], [2, 0], [3, 0]],
    [[-1, 0], [-2, 0], [-3, 0]],
    [[0, 1], [0, 2], [0, 3]],
    [[0, -1], [0, -2], [0, -3]]]

B = [[[0, 1], [1, 1], [1, 0]]]

C = [[[-1, 0], [-1, 1], [-1, 2]],
    [[0, 1], [1, 1], [2, 1]],
    [[1, 0], [1, -1], [1, -2]],
    [[0, -1], [-1, -1], [-2, -1]],
    # 대칭
    [[1, 0], [1, 1], [1, 2]],
    [[0, 1], [-1, 1], [-2, 1]],
    [[-1, 0], [-1, -1], [-1, -2]],
    [[0, -1], [1, -1], [2, -1]]]

D = [[[1, 0], [1, 1], [2, 1]],
    [[0, -1], [1, -1], [1, -2]],
    # 대칭
    [[-1, 0], [-1, 1], [-2, 1]],
    [[0, -1], [-1, -1], [-1, -2]]]


E = [[[0, 1], [0, 2], [1, 1]],
    [[1, 0], [2, 0], [1, -1]],
    [[0, 1], [0, 2], [-1, 1]],
    [[1, 0], [2, 0], [1, 1]]]

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    res = 0
    for i in range(N):
        for j in range(M):
            fix = arr[i][j]
            # print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
            # A
            for p in range(len(A)):
                temp = fix
                for q in range(len(A[p])):
                    nx = i + A[p][q][0]
                    ny = j + A[p][q][1]
                    if 0 <= nx < N and 0 <= ny < M:
                        temp += arr[nx][ny]
                    else:
                        temp = 0
                        break
                if res < temp:
                    res = temp
            # print(res)    
                
            # print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
            # B
            for p in range(len(B)):
                temp = fix
                for q in range(len(B[p])):
                    nx = i + B[p][q][0]
                    ny = j + B[p][q][1]
                    if 0 <= nx < N and 0 <= ny < M:
                        temp += arr[nx][ny]
                if res < temp:
                    res = temp
            # print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
            # C            
            for p in range(len(C)):
                temp = fix
                for q in range(len(C[p])):
                    nx = i + C[p][q][0]
                    ny = j + C[p][q][1]
                    if 0 <= nx < N and 0 <= ny < M:
                        temp += arr[nx][ny]
                if res < temp:
                    res = temp
            # print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
            # D
            for p in range(len(D)):
                temp = fix
                for q in range(len(D[p])):
                    nx = i + D[p][q][0]
                    ny = j + D[p][q][1]
                    if 0 <= nx < N and 0 <= ny < M:
                        temp += arr[nx][ny]
                if res < temp:
                    res = temp
            # print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
            # E
            for p in range(len(E)):
                temp = fix
                for q in range(len(E[p])):
                    nx = i + E[p][q][0]
                    ny = j + E[p][q][1]
                    if 0 <= nx < N and 0 <= ny < M:
                        temp += arr[nx][ny]
                if res < temp:
                    res = temp
            # print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    
    # print(f'#{tc} {res}')
    print(res)