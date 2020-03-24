import sys; sys.stdin = open("graph triangle.txt", "r")

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]

    visit = [0] * (N+1)
    res = 0
    for i in range(len(arr)):
        if visit[arr[i][0]] == 0:
            stack = []
            stack.append(arr[i][0])
            while stack:
                x = stack.pop()
                visit[x] = 1
                for j in range(len(arr)):
                    if arr[j][0] == x and visit[arr[j][1]] == 0:
                        stack.append(arr[j][0])
                    if arr[j][0] == x and visit[arr[j][1]] == 0:
                        stack.append(arr[j][1])
            res += 1

    print(f'#{tc} {res}')