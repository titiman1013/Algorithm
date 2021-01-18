import sys; sys.stdin = open('text1.txt', 'r')

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def diffusion(clone):
    temp_lst = [[0] * C for _ in range(R)]
    cleaners = [] 
    for i in range(R):
        for j in range(C):
            if clone[i][j] > 0:
                move_dust = clone[i][j] // 5
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < R and 0 <= ny < C:
                        if clone[nx][ny] >= 0:
                            temp_lst[nx][ny] += move_dust
                            cnt += 1
                temp_lst[i][j] += clone[i][j] - move_dust * cnt
            elif clone[i][j] == -1:
                temp_lst[i][j] = -1
                cleaners.append((i, j))
    return temp_lst, cleaners


def move(clone, cleaners):
    temp_lst = [[0] * C for _ in range(R)]
    



for tc in range(1, int(input()) + 1):
    R, C, T = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(R)]

    for time in range(T):
        arr, cleaners = diffusion(arr)
        move(arr, cleaners)