import sys; sys.stdin = open('calculate.txt', 'r')

# #
# def check(number, cnt):
#     global res

#     if number == M:
#         if cnt < res:
#             res = cnt
#             return
    
#     if cnt > res:
#         return

#     if number > 1000000:
#         return

#     for i in range(4):
#         if i == 2:
#             # if number * 2 not in lis:
#             #     lis.append(number*2)
#             check(number*2, cnt+1)
#         else:
#             # if number + arr[i] not in lis:
#                 # lis.append(number+arr[i])
#             check(number+arr[i], cnt+1)


# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     arr = [1, -1, 2, -10]

#     res = 1000000
#     lis = []
#     check(N, 0)

#     print(f'#{tc} {res}')


#
from collections import deque

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [1, -1, 2, -10]

    que = deque()
    que.append((N, 0))
    num_list = []
    res = 1000000
    while que:
        x, y = que.popleft()
        if x == M:
            if y < res:
                res = y
        if x > 1000000:
            continue
        if y > res:
            continue
        if x in num_list:
            continue
        for k in range(4):
            if k == 2:
                nx = x * 2
            else:
                nx = x + arr[k]
            que.append((nx, y+1))

    print(f'#{tc} {res}')