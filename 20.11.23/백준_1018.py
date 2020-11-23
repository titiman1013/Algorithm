import sys; sys.stdin = open('text3.txt', 'r')

# def check(x, y):
#     temp = 0
#     color = ''
#     for p in range(8):
#         for q in range(8):
#             if p == 0 and q == 0:
#                 color = arr[x + p][y + q]
#                 continue
#             if arr[x + p][y + q] == color:
#                 temp += 1
#                 if color == 'W':
#                     color = 'B'
#                 else:
#                     color = 'W'
#                 if temp > res:
#                     return False
#             else:
#                 color = arr[x + p][y + q]
#                 continue
#         if color == 'W':
#             color = 'B'
#         else:
#             color = 'W'
#     return temp


def check(x, y, color):
    temp = 0
    for p in range(8):
        for q in range(8):
            if p == 0 and q == 0:
                continue
            if arr[x + p][y + q] == color:
                temp += 1
                if color == 'W':
                    color = 'B'
                else:
                    color = 'W'
                if temp > res:
                    return False
            else:
                color = arr[x + p][y + q]
                continue
        if color == 'W':
            color = 'B'
        else:
            color = 'W'
    return temp




for tc in range(6):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    res = 10000000000

    for i in range(N - 8 + 1):
        for j in range(M - 8 + 1):
            ischeck = check(i, j, 'W')
            if ischeck == False:
                pass
            else:
                if ischeck < res:
                    if arr[i][j] == 'W':
                        res = ischeck
                    else:
                        res = ischeck + 1
            ischeck2 = check(i, j, 'B')
            if ischeck2 == False:
                continue
            else:
                if ischeck2 < res:
                    if arr[i][j] == 'B':
                        res = ischeck2
                    else:
                        res = ischeck2 + 1
            
    print(tc, res)