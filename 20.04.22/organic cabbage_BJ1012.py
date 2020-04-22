import sys; sys.stdin = open('organic cabbage.txt', 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(1, int(input())+1):
    M, N, K = map(int, input().split())
    # M 은 가로길이 N 은 세로길이 K 는 배추 심은 위치개수
    cabbages = [list(map(int, input().split())) for _ in range(K)]

    arr = [[0] * M for _ in range(N)]
    for y, x in cabbages:
        arr[x][y] = 1
    # print(arr)

    res = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                res += 1
                stack = [(i, j)]
                arr[i][j] = 0
                while stack:
                    x, y = stack.pop()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < M:
                            if arr[nx][ny] == 1:
                                stack.append((nx, ny))
                                arr[nx][ny] = 0

    print(f'#{tc} {res}')
    # print(res)



# 답
# 1 5
# 2 1
# 3 2



#
# for tc in range(1, int(input())+1):
#     M, N, K = map(int, input().split())
#     cabbages = [list(map(int, input().split())) for _ in range(K)]

#     stack = [cabbages[0]]
#     a = 1
#     while stack:
#         x, y = stack.pop()
#         if 