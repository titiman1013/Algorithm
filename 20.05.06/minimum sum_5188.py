import sys; sys.stdin = open('minimum sum.txt', 'r')

#
def go(x, y, sum):
    global minimum
    if 0 <= x < N and 0 <= y < N:
        if x == N - 1 and y == N - 1:
            sum += arr[x][y]
            if sum < minimum:
                minimum = sum
            return
        else:
            if sum > minimum:
                return

        go(x+1, y, sum+arr[x][y])
        go(x, y+1, sum+arr[x][y])



for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    minimum = 1000000
    go(0, 0, 0)
    print(f'#{tc} {minimum}')


#
# for tc in range(1, int(input())+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]

#     x = 0
#     y = 0
#     res = arr[x][y]
#     while True:
#         if x == N - 1 and y == N - 1:
#             break
#         if x != N - 1 and y != N - 1:
#             if arr[x+1][y] < arr[x][y+1]:
#                 res += arr[x+1][y]
#                 x += 1
#             else:
#                 res += arr[x][y+1]
#                 y += 1
#         elif x == N - 1 and y != N - 1:
#             res += arr[x][y+1]
#             y += 1
#         elif x != N - 1 and y == N - 1:
#             res += arr[x+1][y]
#             x += 1

#     print(f'#{tc} {res}')