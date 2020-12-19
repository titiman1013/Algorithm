import sys; sys.stdin = open('text1.txt', 'r')

def network_connet():
    for i in range(M):
        x, y = arr[i][0] - 1, arr[i][1] - 1
        network[x][y] = 1
        network[y][x] = 1
    return


def virus():
    stack = [0]
    while stack:
        x = stack.pop()
        for k in range(N):
            if network[x][k]:
                if res_list[k] == 0:
                    res_list[k] = 1
                    stack.append(k)



for tc in range(1, int(input()) + 1):
    N = int(input())
    M = int(input())
    arr = [list(map(int, input().split())) for _ in range(M)]

    res_list = [0] * N
    network = [[0] * N for _ in range(N)]
    network_connet()
    virus()
    res = 0
    for i in range(N):
        if res_list[i]:
            res += 1
    print(res - 1)