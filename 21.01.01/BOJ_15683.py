import sys; sys.stdin = open('text1.txt', 'r')

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def check():
    global res

    sum_temp = 0
    for i in range(N):
        for j in range(M):
            if 0 < arr[i][j] < 6:
                sum_lst = go(i, j)


def go(start_x, start_y):
    stack = [(start_x, start_y)]
    temp_sum_lst = []
    for k in range(4):
        sum = arr[start_x][start_y]
        while True:
            cnt = 0
            nx = start_x + dx[k]
            ny = start_y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0:
                    sum += arr[nx][ny]
                    cnt += 1
                elif 0 < arr[nx][ny] < 6:
                    cnt += 1
            if cnt == 0:
                break


# def calc(temp_arr):
#     temp = 0
#     for i in range(N):
#         for j in range(M):
#             if temp_arr[i][j] == 0:
#                 temp += 1
#     return temp



for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    # 0: 빈 칸, 1: 한 방향, 2: 양 방향, 3: 직각 방향, 4: 세 방향, 5: 전 방향, 6: 벽, 7: cctv로 변환된 곳, 8: 보이는 시야
    arr = [list(map(int, input().split())) for _ in range(N)]

    res = 8 ** 2 + 1