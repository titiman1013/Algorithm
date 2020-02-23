# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# N = int(input())
# arr = [list(map(int, list(input()))) for i in range(N)]

# # cnt = 0
# # for i in range(N):
# #     for j in range(N):
# #         if arr[i][j] == 1:
# #             cnt += 1

# # visit = [[0] * (cnt+1)]
# cnt_list = []
# color = 0
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == 1:
#             color += 1
#             stack = []
#             stack.append((i,j))
#             while stack:
#                 cnt = 0
#                 start = stack.pop(-1)
#                 x = start[0]
#                 y = start[1]
#                 if arr[x][y] != 0:
#                     nx = 0 
#                     ny = 0
#                     cnt += 1
#                     arr[x][y] = 0
#                     for k in range(4):
#                         nx = x + dx[k]
#                         ny = y + dy[k]
#                         if 0 <= nx < N-1 and 0 <= ny < N-1: 
#                             if arr[nx][ny] != 0:
#                                 x = nx
#                                 y = ny
#                                 break
#             cnt_list.append(cnt)
#             break

# cnt_list.sort()
# print(color)
# for i in range(len(cnt_list)):
#     print(i)

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# N = int(input())
# arr = [list(map(int, list(input()))) for i in range(N)]

# cnt_list = []
# color = 0
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == 1:
#             color += 1
#             cnt = 0
#             stack = []
#             stack.append([i,j])
#             arr[i][j] = 0
#             x = i
#             y = j
#             while stack:
#                 if arr[x][y] == 1:
#                     cnt += 1
#                     for k in range(4):
#                         nx = x + dx[k]
#                         ny = y + dy[k]
#                         if arr[nx][ny] == 1:
#                             x = nx
#                             y = ny
#                             arr[nx][ny] = 0
#                             stack.append([nx, ny])
#                             break
#                     else:
#                         x = stack[-1][0]
#                         y = stack[-1][1]
#             cnt_list.append(cnt)

# print(color)
# for i in cnt_list:
#     print(i)



# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# N = int(input())
# arr = [list(map(int, list(input()))) for i in range(N)]

# r_list = []

# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == 1:
#             cnt = 1
#             arr[i][j] = 0
#             x = i
#             y = j
#             stack = [[x,y]]
#             while stack:
#                 for k in range(4):
#                     nx = x + dx[k]
#                     ny = y + dy[k]
#                     if 0 <= nx < N and 0 <= ny < N:
#                         if arr[nx][ny] == 1:
#                             stack.append([nx, ny])
#                             cnt += 1
#                             arr[nx][ny] = 0
#                             x = nx
#                             y = ny
#                 else:
#                     x = stack[-1][0]
#                     y = stack[-1][1]
#                     stack.pop() 
#             r_list.append(cnt)

# r_list.sort()
# print(len(r_list))
# for i in range(len(r_list)):
#     print(r_list[i])


# 정답
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N = int(input())
arr = [list(map(int, list(input()))) for i in range(N)]
r_list = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt = 1
            arr[i][j] = 0
            x = i
            y = j
            stack = [[x,y]]
            while stack:
                x, y =stack.pop() 
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if arr[nx][ny] == 1:
                            stack.append([nx, ny])
                            cnt += 1
                            arr[nx][ny] = 0
                            
                # else:
                    # x = stack[-1][0]
                    # y = stack[-1][1] 밑 한줄이랑 똑같음
                    
            r_list.append(cnt)
r_list.sort()
print(len(r_list))
for i in range(len(r_list)):
    print(r_list[i])