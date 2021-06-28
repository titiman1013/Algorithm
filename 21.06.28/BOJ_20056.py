import sys; sys.stdin = open('20056.txt', 'r')

#

# import sys


# input = sys.stdin.readline
# dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

# for tc in range(1, int(input()) + 1):
#     N, M, K = map(int, input().split())
#     fireball_infos = [list(map(int, input().split())) for _ in range(M)]

#     arr = [[[] for _ in range(N)] for _ in range(N)]
#     for _ in range(K):
#         tmp_fireball_infos = []
#         tmp_arr = [[[] for _ in range(N)] for _ in range(N)]
#         print(fireball_infos)
#         for x, y, m, s, d in fireball_infos:
#             tmp_arr[(x - 1 + dx[d] * s) % N][(y - 1 + dy[d] * s) % N].append([m, s, d])
        
#         for i in range(N):
#             for j in range(N):
#                 if arr[i][j]:
#                     sum_m = 0
#                     sum_s = 0
#                     d_infos = []
#                     for m, s, d in arr[i][j]:
#                         sum_m += m
#                         sum_s += s
#                         if d % 2:
#                             d_infos.append(True)
#                         else:
#                             d_infos.append(False)
#                     if sum_m // 5:
#                         if d_infos.count(True) == len(arr[i][j]) or d_infos.count(False) == len(arr[i][j]):
#                             for tmp_d in range(0, 7, 2):
#                                 tmp_fireball_infos.append([i + 1, j + 1, sum_m // 5, sum_s // len(arr[i][j]), tmp_d])
#                         else:
#                             for tmp_d in range(1, 8, 2):
#                                 tmp_fireball_infos.append([i + 1, j + 1, sum_m // 5, sum_s // len(arr[i][j]), tmp_d])

#         for x, y, m, s, d in tmp_fireball_infos:
#             tmp_arr[x - 1][y - 1].append([m, s, d])
#         fireball_infos = tmp_fireball_infos
#         arr = tmp_arr

#         for val in arr:
#             print(val)
#         print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡ한번ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
#     answer = sum(m for x, y, m, s, d in fireball_infos)
#     print(answer)
#     print('ㅡㅡㅡㅡㅡㅡㅡㅡ끝ㅡㅡㅡㅡㅡㅡㅡㅡㅡ')




#

import sys


input = sys.stdin.readline
dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

def move():
    global fireball_infos, arr
    
    tmp_arr = [[[] for _ in range(N)] for _ in range(N)]
    tmp_infos = []
    for x, y, m, s, d in fireball_infos:
        nx, ny = (x - 1 + dx[d] * s) % N, (y - 1 + dy[d] * s) % N
        tmp_arr[nx][ny].append([m, s, d])
        tmp_infos.append([nx + 1, ny + 1, m, s, d])
    
    fireball_infos = tmp_infos
    arr = tmp_arr
    return


def divide():
    global fireball_infos
    
    tmp_infos = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                if len(arr[i][j]) > 1:
                    sum_m, sum_s = 0, 0
                    ds = []
                    while arr[i][j]:
                        m, s, d = arr[i][j].pop()
                        sum_m += m
                        sum_s += s
                        ds.append('홀수' if d % 2 else '짝수')
                        # if d % 2:
                        #     ds.append('홀수')
                        # else:
                        #     ds.append('짝수')
                    
                    if sum_m // 5:
                        if ds.count('홀수') == len(ds) or ds.count('짝수') == len(ds):
                            next_ds = [0, 2, 4, 6]
                        else:
                            next_ds = [1, 3, 5, 7]
                        for next_d in next_ds:
                            arr[i][j].append([sum_m // 5, sum_s // len(ds), next_d])
                            tmp_infos.append([i + 1, j + 1, sum_m // 5, sum_s // len(ds), next_d])
                else:
                    tmp_infos.append([i + 1, j + 1, *arr[i][j][0]])
    fireball_infos = tmp_infos
    return


def calc_sum():
    return sum(m for x, y, m, s, d in fireball_infos)



for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    fireball_infos = [list(map(int, input().split())) for _ in range(M)]

    arr = [[[] for _ in range(N)] for _ in range(N)]
    for x, y, m, s, d in fireball_infos:
        arr[x - 1][y - 1].append([m, s, d])

    for _ in range(K):
        # print(fireball_infos)
        # for val in arr:
        #     print(val)
        # print('ㅡㅡㅡㅡㅡㅡ원본ㅡㅡㅡㅡㅡ')
        move()
        # for val in arr:
        #     print(val)
        # print('ㅡㅡㅡㅡㅡㅡ이동ㅡㅡㅡㅡㅡ')
        divide()
        # for val in arr:
        #     print(val)
        # print('ㅡㅡㅡㅡㅡㅡ분할ㅡㅡㅡㅡㅡ')
    
    answer = calc_sum()
    # print(fireball_infos)
    print(answer)