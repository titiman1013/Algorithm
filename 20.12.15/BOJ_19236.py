import sys; sys.stdin = open('text1.txt', 'r')

dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]


def order_fish():
    temp_arr = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        temp = 0
        for j in range(8):
            if i == 0 and j == 0:
                temp_arr[i][temp].append('shark')
                continue
            temp_arr[i][temp].append(arr[i][j])
            if j % 2 == 1:
                temp += 1
                if temp >= 4:
                    temp = 0

    return temp_arr


def recursive():
    if shark_move(i, j) == True:
        return res


def fish_move():
    pass


def shark_move(i, j):
    pass



for tc in range(1, int(input()) + 1):
    # ai, bi: 물고기번호, 방향
    # 4 4 행렬이라 생각
    arr = [list(map(int, input().split())) for _ in range(4)]
    
    arr = order_fish()
    