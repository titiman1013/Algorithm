import sys; sys.stdin = open('text1.txt', 'r')


def create_list():
    for i in range(M):
        x, y = arr[i][0] - 1, arr[i][1] - 1
        pd_list[x][y] = 1
        pd_list[y][x] = 1
    return


def search():
    temp_res = 0
    stack = [A - 1]
    while stack:
        x = stack.pop()
        for k in range(N):
            if pd_list[x][k] == 1:
                if k == B - 1:
                    relation[k] = relation[x] + 1
                    return relation[k]
                elif relation[k] == 0:
                    relation[k] = relation[x] + 1
                    stack.append(k)
    return -1



for tc in range(1, int(input()) + 1):
    N = int(input())
    A, B = map(int, input().split())
    M = int(input())
    arr = [list(map(int, input().split())) for _ in range(M)]

    # parents & daughter list
    pd_list = [[0] * N for _ in range(N)]
    # family relation
    relation = [0] * N
    
    create_list()
    res = search()
    print(res)