import sys; sys.stdin = open('sudoku.txt', 'r')

# 1
for tc in range(1, int(input()) + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    # 행 우선, 열 우선, 3 x 3 사각 영역
    for i in range(9):
        # 매행을 시작할 때 초기화가 필요한 작업
        row = [0] * 10  # 1 ~ 9
        col = [0] * 10
        for j in range(9):
            if row[arr[i][j]]: break
            if col[arr[j][i]]: break
            row[arr[i][j]] = col[arr[j][i]] = 1
        # 그 행이 작업이 끝나고, 정리하는 작업

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):

            # 왼쪽 모서리 (i, j)에서 높이 = 너비 = 3
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    arr[x][y]

# 2
for tc in range(1, int(input()) + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    def lineCheck():
        for i in range(9):
        # 매행을 시작할 때 초기화가 필요한 작업
            row = [0] * 10  # 1 ~ 9
            col = [0] * 10
            for j in range(9):
                if row[arr[i][j]] or col[arr[j][i]]: return 0
                row[arr[i][j]] = col[arr[j][i]] = 1
        return 1

    def rectcheck():
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                rect = [0] * 10
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        if rect[arr[x][y]]: return 0
                        rect[arr[x][y]] = 1
        return 1