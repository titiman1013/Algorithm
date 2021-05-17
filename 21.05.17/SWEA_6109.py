import sys; sys.stdin = open('6109.txt', 'r')

def rotate(tmp_arr):
    return [list(elem) for elem in zip(*tmp_arr[::-1])]


def calc(tmp_arr, N):
    for i in range(N):
        for j in range(N - 1):
            if tmp_arr[j][i]:
                if tmp_arr[j][i] == tmp_arr[j + 1][i]:
                    tmp_arr[j][i] *= 2
                    tmp_arr[j + 1][i] = 0
                elif tmp_arr[j + 1][i] == 0:
                    tmp_j = j + 1
                    while tmp_j < N - 1 and tmp_arr[tmp_j][i] == 0:
                        tmp_j += 1
                    if tmp_arr[j][i] == tmp_arr[tmp_j][i]:
                        tmp_arr[j][i] += 2
                        tmp_arr[tmp_j][i] = 0
    return tmp_arr


def move_zero(tmp_arr, N):
    for i in range(N):
        for j in range(N - 1):
            if tmp_arr[j][i] == 0:
                tmp_j = j + 1
                while tmp_j < N - 1 and tmp_arr[tmp_j][i] == 0:
                    tmp_j += 1
                tmp_arr[j][i] = tmp_arr[tmp_j][i]
                tmp_arr[tmp_j][i] = 0
    return tmp_arr


def move(tmp_arr, N):
    tmp_arr = move_zero(calc(move_zero(tmp_arr, N), N), N)

    return tmp_arr



for tc in range(1, int(input()) + 1):
    N, S = map(str, input().split())
    boards = list(list(map(int, input().split())) for _ in range(int(N)))

    commands = {
        "up": 0,
        "left": 1,
        "down": 2,
        "right": 3,
    }
    for _ in range(commands.get(S)):
        boards = rotate(boards)
    boards = move(boards, int(N))
    for _ in range(4 - commands.get(S)):
        boards = rotate(boards)
    
    print(f'#{tc}')
    for i in range(int(N)):
        for j in range(int(N)):
            print(boards[i][j], end=' ')
        print()