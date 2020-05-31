import sys; sys.stdin = open('lookslike russia flag.txt', 'r')

#
# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     arr = list(input() for _ in range(N))

#     res = 0
#     color = 0
#     # color가 0일땐 white, 1일땐 blue, 2일땐 red
#     for i in range(N):
#         white = 0
#         blue = 0
#         red = 0
#         for j in range(M):
#             if arr[i][j] == 'W':
#                 white += 1
#             elif arr[i][j] == 'B':
#                 blue += 1
#             else:
#                 red += 1
        
#         if i == 0:
#             res += blue
#             res += red
#         else:
#             if color == 0:
#                 if white > blue:
#                     if i + 1 < N - 2:
#                         res += blue
#                         red += red
#                     else:
#                         res += white
#                         res += red
#                         color += 1
#                 else:
#                     res += white
#                     res += red
#                     color += 1
#             elif color == 1:
#                 if blue > red:
#                     if i + 1 < N - 1:
#                         res += white
#                         res += red
#                     else:
#                         res += white
#                         res += blue
#                         color += 1
#                 else:
#                     res += white
#                     res += blue
#                     color += 1
#             elif color == 2:
#                 res += white
#                 res += blue
    
#         print(res)
    
#     print(f'#{tc} {res}')



#
def check(cnt, color, _sum):
    global res

    if cnt == N:
        if _sum < res:
            res = _sum
        return

    if cnt == 0:
        for i in range(M):
            if arr[cnt][i] != 'W':
                _sum += 1
        check(cnt+1, color, _sum)
    else:
        white = 0
        blue = 0
        red = 0
        for i in range(M):
            if arr[cnt][i] == 'W':
                white += 1
            elif arr[cnt][i] == 'B':
                blue += 1
            else:
                red += 1

        if color == 0:
            pass
        elif color == 1:
            pass
        else:
            _sum += white + blue
            check(cnt+1, color, _sum)





for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    res = 0
    check(0, 0, 0)