import sys; sys.stdin = open('robotic vacuum.txt', 'r')

#
# dx = [0, -1, 0, 1]
# dy = [-1, 0, 1, 0]

# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     now_x, now_y, direction = map(int, input().split())
#     # 0: 북, 1: 동, 2: 남, 3: 서
#     arr = [list(map(int, input().split())) for _ in range(N)]

#     res = 0
#     stack = [(now_x, now_y, direction)]
#     while stack:
#         # print(stack)
#         x, y, direction = stack.pop()
#         arr[x][y] = 2
#         res += 1
#         cnt = 0
#         for k in range(direction, direction-4, -1):
#             if k < -3:
#                 k += 4
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < N and 0 <= ny < M:
#                 if arr[nx][ny] == 0:
#                     stack.append((nx, ny, k-1))
#                     cnt += 1
#                     break
#         if cnt == 0:
#             if arr[x-dx[direction]][y-dx[direction]] == 2:
#                 stack.clear()
#                 stack.append((x-dx[direction], y-dx[direction], direction))
#             elif arr[x-dx[direction]][y-dx[direction]] == 1:
#                 break
#         print(res)
#         print(arr)
#         print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
#         if res > 50:
#             break

#     print(f'#{tc} {res}')


# #
# dx = [0, 1, 0, -1]
# dy = [-1, 0, 1, 0]

# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     x, y, direction = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]

#     arr[x][y] = 2
#     res = 1
#     while True:
#         cnt = 0
#         for k in range(4):
#             if k + direction > 3:
#                 a = k + direction - 4
#             else:
#                 a = k + direction
#             nx = x + dx[a]
#             ny = y + dy[a]
#             if 0 <= nx < N and 0 <= ny < M:
#                 if arr[nx][ny] == 0:
#                     arr[nx][ny] = 2
#                     x = nx
#                     y = ny
#                     cnt += 1
#                     res += 1
#                     if a == 0:
#                         direction = 1
#                     elif a == 1:
#                         direction = 2
#                     elif a == 2:
#                         direction = 3
#                     else:
#                         direction = 0
#                     break
#         if cnt == 0:
#             if a == 0:
#                 if arr[x+1][y] == 2:
#                     x = x + 1
#                     direction = 2
#             elif a == 1:
#                 if arr[x][y+1] == 2:
#                     y = y + 1
#                     direction = 3
#             elif a == 2:
#                 if arr[x-1][y] == 2:
#                     x = x - 1
#                     direction = 0
#             else:
#                 if arr[x][y-1] == 2:
#                     y = y - 1
#                     direction = 1
#             break
#         print(arr)
#         print(x, y)
#         print(direction)

    
#     print(f'#{tc} {res}')

#
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    x, y, direction = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    res = 1
    while True:
        arr[x][y] = 2
        if direction == 0:
            start = 0
        elif direction == 1:
            start = 3
        elif direction == 2:
            start = 2
        elif direction == 3:
            start = 1
        
        for k in range(start, start+4):
            if k > 3:
                k -= 4
            nx = x + dx[k]
            ny = y + dy[k]
            direction -= 1
            if direction < 0:
                direction += 4
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0:
                    x = nx
                    y = ny
                    res += 1
                    break
                
# dx = [0, 1, 0, -1]
# dy = [-1, 0, 1, 0]

        else:
            if direction == 0 or direction == 2:
                if arr[x+dx[direction+1]][y+dy[direction+1]] == 2:
                    x = x + dx[direction+1]
                    y = y + dy[direction+1]
                elif arr[x+dx[direction+1]][y+dy[direction+1]] == 1:
                    break
            else:
                if arr[x+dx[direction-1]][y+dy[direction-1]] == 2:
                    x = x + dx[direction-1]
                    y = y + dy[direction-1]
                elif arr[x+dx[direction-1]][y+dy[direction-1]] == 1:
                    break

        # print(x, y)
        # print(res, direction)
        
    
    print(f'#{tc} {res}')