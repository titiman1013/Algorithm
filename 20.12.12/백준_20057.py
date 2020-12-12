import sys; sys.stdin = open('text1.txt', 'r')

# dx = [-2, -1, -1, -1, 0, 1, 1, 1, 2]
# dy = [0, -1, 0, 1, -2, -1, 0, 1, 0]
# per = [2, 10, 7, 1, 5, 10, 7, 1, 2]

# def calc_cnt(N):
#     # N = 5
#     # [1, 1, 2, 2, 3, 3, 4, 4, 4]
#     cnt_list = []
#     for i in range(N):
#         if i != N - 1 and i != 0:
#             for _ in range(2):
#                 cnt_list.append(i)
#         elif i == N - 1:
#             for _ in range(3):
#                 cnt_list.append(i)
#     return cnt_list


# def wind(x, y):
#     global res
    
#     sand = arr[x][y]
#     blowed_sand = 0
#     for i in range(9):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         temp = int(sand * (per[i] / 100))
#         blowed_sand += temp
#         if 0 <= nx < N and 0 <= ny < N:
#             arr[nx][ny] += temp
#         else:
#             res += temp
#     arr[x][y] = 0
#     arr[x][y - 1] = sand - blowed_sand
#     return position_x, position_y - 1


# # 시계방향으로 한 번 회전
# def turn_arr():
#     temp_arr = list(map(list, zip(*arr)))
#     return temp_arr



# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     arr= [list(map(int, input().split())) for _ in range(N)]

#     res = 0
#     cnt_list = calc_cnt(N)
#     position_x = N // 2
#     position_y = N // 2
#     # 0: 좌, 1: 하, 2: 우, 3: 상
#     direction = 0

#     for i in cnt_list:
#         for move in range(i):
#             position_x, position_y = wind(position_x, position_y)
#         temp_x = position_x
#         position_x = position_y
#         position_y = temp_x
#         arr = turn_arr()

#     print(f'#{tc} {res}')


