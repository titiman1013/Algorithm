import sys; sys.stdin = open("section search.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(1, int(input())+1):
    M, N, K = map(int, input().split())
    # x(i)가 N, y(j)가 M
    in_box = [list(map(int, input().split())) for _ in range(K)]
    arr = [[0] * M for _ in range(N)]

    for l in range(len(in_box)):
        for i in range(N):
            for j in range(M):
                if in_box[l][0] <= i < in_box[l][2] and in_box[l][1] <= j < in_box[l][3]:
                    arr[i][j] = 1

    cnt = 0
    cnt_list = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                cnt += 1
                temp = 0
                stack = [(i, j)]
                arr[i][j] = 1
                while stack:
                    x, y = stack.pop()
                    temp += 1
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < M:
                            if arr[nx][ny] == 0:
                                stack.append((nx, ny))
                                arr[nx][ny] = 1
                cnt_list.append(temp)

    cnt_list.sort()
    print(cnt)
    for i in range(len(cnt_list)):
        print(cnt_list[i], end=' ')
    print()