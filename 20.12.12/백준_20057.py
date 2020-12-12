import sys; sys.stdin = open('text1.txt', 'r')

# solve test1 fail
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


# solve test2
dx = [-2, -1, -1, -1, 0, 1, 1, 1, 2]
dy = [-1, -2, -1, 0, -3, -2, -1, 0, -1]
per = [2, 10, 7, 1, 5, 10, 7, 1, 2]

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 1: 좌, 2: 하, 3: 우, 4: 상
    direction = 1
    x = N // 2
    y = N // 2
    res = 0
    move_list = []
    for i in range(N):
        if i != N - 1 and i != 0:
            for _ in range(2):
                move_list.append(i)
        elif i == N - 1:
            for _ in range(3):
                move_list.append(i)

    for move in move_list:
        for _ in range(move):
            if direction == 1:
                if y - 1 < 0:
                    res += arr[x][y]
                else:
                    sand = arr[x][y - 1]
                    blowed_sand = 0
                    for i in range(9):
                        nx = x + dx[i]
                        ny = y + dy[i] - 1
                        # temp_sand = int(arr[x][y] * (per[i] / 100))
                        temp_sand = (sand * per[i]) // 100
                        if 0 <= nx < N and 0 <= ny < N:
                            arr[nx][ny] += temp_sand
                        else:
                            res += temp_sand
                        blowed_sand += temp_sand
                    arr[x][y - 1] = 0
                    y -= 1
                    arr[x][y - 1] += (sand - blowed_sand)
                    
            elif direction == 2:
                if x + 1 >= N:
                    res += arr[x][y]
                else:
                    sand = arr[x + 1][y]
                    blowed_sand = 0
                    for i in range(9):
                        nx = x - dy[i] + 1
                        ny = y + dx[i]
                        # temp_sand = int(arr[x][y] * (per[i] / 100))
                        temp_sand = (sand * per[i]) // 100
                        if 0 <= nx < N and 0 <= ny < N:
                            arr[nx][ny] += temp_sand
                        else:
                            res += temp_sand
                        blowed_sand += temp_sand
                    arr[x + 1][y] = 0
                    x += 1
                    arr[x + 1][y] += (sand - blowed_sand)

            elif direction == 3:
                if y + 1 >= N:
                    res += arr[x][y]
                else:
                    sand = arr[x][y + 1]
                    blowed_sand = 0
                    for i in range(9):
                        nx = x - dx[i]
                        ny = y - dy[i] + 1
                        # temp_sand = int(arr[x][y] * (per[i] / 100))
                        temp_sand = (sand * per[i]) // 100
                        if 0 <= nx < N and 0 <= ny < N:
                            arr[nx][ny] += temp_sand
                        else:
                            res += temp_sand
                        blowed_sand += temp_sand
                    arr[x][y + 1] = 0
                    y += 1
                    arr[x][y + 1] += (sand - blowed_sand)

            elif direction == 4:
                if x - 1 < 0:
                    res += arr[x][y]
                else:
                    sand = arr[x - 1][y]
                    blowed_sand = 0
                    for i in range(9):
                        nx = x - dy[i] - 1
                        ny = y - dx[i]
                        # temp_sand = int(arr[x][y] * (per[i] / 100))
                        temp_sand = (sand * per[i]) // 100
                        if 0 <= nx < N and 0 <= ny < N:
                            arr[nx][ny] += temp_sand
                        else:
                            res += temp_sand
                        blowed_sand += temp_sand
                    arr[x - 1][y] = 0
                    x -= 1
                    arr[x - 1][y] += (sand - blowed_sand)

        direction += 1
        if direction == 5:
            direction = 1
    
    print(f'#{tc} {res}')
    print(arr)