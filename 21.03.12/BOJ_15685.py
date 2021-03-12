import sys; sys.stdin = open('15685.txt', 'r')

def create(x, y, d):
    if d == 0:
        nx, ny = x + 1, y
    elif d == 1:
        nx, ny = x, y + 1
    elif d == 2:
        nx, ny = x - 1, y
    else:
        nx, ny = x, y - 1

    tmp_lst = ((x, y), (nx, ny))
    co = (nx, ny)

    return tmp_lst, co


def rotate(point_lst, co):
    for point in point_lst:
        pass


def check():
    pass



for tc in range(1, int(input()) + 1):
    N = int(input())
    curves = [list(map(int, input().split())) for _ in range(N)]

    curve_lst = []
    for x, y, d, g in curves:
        # 좌표리스트, 축(coordinate)
        point_lst, co = create(x, y, d)
        for _ in range(g):
            point_lst += rotate(point_lst, co)