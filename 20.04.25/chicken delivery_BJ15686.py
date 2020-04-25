import sys; sys.stdin = open('chicken delivery.txt', 'r')
# from collections import deque

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def check(cnt):
#     while dq:
#         for _ in range(4):
#             x, y = dq.popleft()
#             for k in range(4):
#                 nx = x + dx[k]
#                 ny = y + dy[k]
#                 if 0 <= nx < N and 0 <= ny < N:
#                     if arr[nx][ny] == 2:
#                         return cnt
#                     else:
#                         dq.append((nx, ny))
#         cnt += 1


# for tc in range(1, int(input())+1):
    # N, M = map(int, input().split())
    # arr = [list(map(int, input().split())) for _ in range(N)]


    # res = 0
    # for i in range(N):
    #     for j in range(N):
    #         if arr[i][j] == 1:
    #             dq = deque([])
    #             distance = 0
    #             for k in range(4):
    #                 nx = i + dx[k]
    #                 ny = j + dy[k]
    #                 if 0 <= nx < N and 0 <= ny < N:
    #                     if arr[nx][ny] == 2:
    #                         distance = 1
    #                         break
    #                     else:
    #                         dq.append((nx, ny))
    #             if distance:
    #                 res += 1
    #                 # print((i, j), res)
    #                 continue
    #             else:
    #                 res += check(2)
    #                 # print((i,j), res)

    # print(res)


from itertools import combinations

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    normal_house = []
    chicken_house = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                chicken_house.append((i, j))
            elif arr[i][j] == 1:
                normal_house.append((i, j))

    res = 1000000
    for pick in list(combinations(chicken_house, M)):
        temp = 0
        for i in range(len(normal_house)):
            ttemp = []
            for j in range(M):
                ttemp.append(abs(normal_house[i][0] - pick[j][0]) + abs(normal_house[i][1] - pick[j][1]))
            temp += min(ttemp)
        if temp < res:
            res = temp

    # print(res)
    print(f'#{tc} {res}')

# 답
#1 5
#2 10
#3 11
#4 32