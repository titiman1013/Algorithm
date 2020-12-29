import sys; sys.stdin = open('text1.txt', 'r')


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def check():
    global res

    cnt = 0
    for x in range(N):
        for y in range(N):
            merge_cnt = 0
            merge_lst = []
            total_people = arr[x][y]
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    if L <= abs(arr[x][y] - arr[nx][ny]) <= R:
                        merge_lst.append((nx, ny))
                        total_people += arr[nx][ny]
                        merge_cnt += 1
            if merge_cnt:
                for i, j in merge_lst:
                    arr[i][j] = total_people // (merge_cnt + 1)
                arr[x][y] = total_people // (merge_cnt + 1)
                cnt += 1
    if cnt:
        res += cnt
        check()
    else:
        return



for tc in range(1, int(input()) + 1):
    N, L, R = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    res = 0
    check()
    print(res)