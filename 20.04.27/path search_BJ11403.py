import sys; sys.stdin = open('path search.txt', 'r')

# 시간초과
# for tc in range(1, int(input())+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     res_arr = [[0] * N for _ in range(N)]
    
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 1:
#                 # print('분기')
#                 stack = [(i, j)]
#                 visit = [[False] * N for _ in range(N)]
#                 while stack:
#                     x, y = stack.pop()
#                     visit[x][y] = True
#                     res_arr[i][y] = 1
#                     for k in range(N):
#                         if arr[y][k] == 1 and visit[y][k] == False:
#                             stack.append((y, k))
                            

#     for i in range(N):
#         for j in range(N):
#             print(res_arr[i][j], end=' ')
#         print()


# #
# import copy

# for tc in range(1, int(input())+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     res_arr = [[0] * N for _ in range(N)]
    
#     visit_base = [[False] * N for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 1:
#                 # print('분기')
#                 stack = [(i, j)]
#                 visit = copy.deepcopy(visit_base)
#                 while stack:
#                     x, y = stack.pop()
#                     visit[x][y] = True
#                     res_arr[i][y] = 1
#                     for k in range(N):
#                         if arr[y][k] == 1 and visit[y][k] == False:
#                             stack.append((y, k))
                            

#     for i in range(N):
#         for j in range(N):
#             print(res_arr[i][j], end=' ')
#         print()


# #
# for tc in range(1, int(input())+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     res_arr = [[0] * N for _ in range(N)]
    
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 1:
#                 # print('분기')
#                 stack = [(i, j)]
#                 while stack:
#                     x, y = stack.pop()
#                     res_arr[i][y] = 1
#                     for k in range(N):
#                         if arr[y][k] == 1:
#                             if y != i and k != j:
#                                 stack.append((y, k))
                            
#     for i in range(N):
#         for j in range(N):
#             print(res_arr[i][j], end=' ')
#         print()


#
for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 1 or (arr[i][k] == 1 and arr[k][j] == 1):
                    arr[i][j] = 1

    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()




# 답
#1 
# 1 1 1
# 1 1 1
# 1 1 1
#2
# 1 0 1 1 1 1 1
# 0 0 1 0 0 0 1
# 0 0 0 0 0 0 0
# 1 0 1 1 1 1 1
# 1 0 1 1 1 1 1
# 0 0 1 0 0 0 1
# 0 0 1 0 0 0 0