import sys; sys.stdin = open('battle field.txt', 'r')

for tc in range(1, int(input())+1):
    H, W = map(int, input().split())
    # H 는 높이 W 는 너비, 즉 H x W 의 격자판
    arr = [input() for _ in range(H)]
    N = int(input())
    # N 은 사용자가 넣을 입력 개수
    moves = input()


# #
# def pos(x,y):
#     if x < 0 or x > W-1 or y < 0 or y > H-1 or map_arr[y][x] != '.':
#         return False
#     return True
 
# T = int(input())
# for tc in range(1, T+1):
#     H, W = map(int,input().split())
#     map_arr = [list(input()) for _ in range(H)]
#     N = int(input())
#     N_list = list(input())
#     dx = [0, 0, -1, 1]
#     dy = [-1, 1, 0, 0]
#     front = 0
 
#     temp_end = False
#     for j in range(H):
#         for i in range(W):
#             start_x, start_y = i, j
#             if map_arr[j][i] == '^':
#                 front = 0
#                 temp_end = True
#             elif map_arr[j][i] == 'v':
#                 front = 1
#                 temp_end = True
#             elif  map_arr[j][i] == '<':
#                 front = 2
#                 temp_end = True
#             elif map_arr[j][i] == '>':
#                 front = 3
#                 temp_end = True
#             if temp_end:
#                 break
#         if temp_end:
#             break
     
#     for k in range(len(N_list)):
#         if N_list[k] == 'U':
#             front = 0
#         elif N_list[k] == 'D':
#             front = 1
#         elif N_list[k] == 'L':
#             front = 2
#         elif N_list[k] == 'R':
#             front = 3
 
#         if N_list[k] == 'S':
#             shot_x = start_x + dx[front]
#             shot_y = start_y + dy[front]
#             while 1:
#                 if shot_x < 0 or shot_x > W-1 or shot_y < 0 or shot_y > H-1:
#                     break
#                 elif map_arr[shot_y][shot_x] == '*':
#                     map_arr[shot_y][shot_x] = '.'
#                     break
#                 elif map_arr[shot_y][shot_x] == '#':
#                     break
#                 else:
#                     shot_x += dx[front]
#                     shot_y += dy[front]
#         elif pos(start_x+dx[front], start_y+dy[front]):
#             map_arr[start_y][start_x] = '.'
#             start_x += dx[front]
#             start_y += dy[front]
 
#         if front == 0:
#             map_arr[start_y][start_x] = '^'
#         elif front == 1:
#             map_arr[start_y][start_x] = 'v'
#         elif front == 2:
#             map_arr[start_y][start_x] = '<'
#         elif front == 3:
#             map_arr[start_y][start_x] = '>'
 
#     print('#{}'.format(tc), end=' ')
#     for n in range(H):
#         print(''.join(map_arr[n]))
 