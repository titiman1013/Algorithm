import sys; sys.stdin = open('binary2.txt', 'r')

# def check(cnt, _sum, res):
#     for i in range(len(N)):

    
#     if _sum == int(N):
#         return 1
#     if cnt == 13:
#         return 0

    


# for tc in range(1, int(input())+1):
#     print(f'#{tc}', end=' ')
#     N = input()[2:]
#     res = []
#     if check(1, 0):
#         for i in range(len(res)):
#             print(res[i], end='')
#         print()
#     else:
#         print('overflow')

for tc in range(1, int(input())+1):
    N = float(input())
    
    res = ''
    cnt = 1
    while True:
        N = N * 2
        if N == 1:
            res += '1'
            break
        elif N > 1:
            res += '1'
            N -= 1
        else:
            res += '0'
        if cnt == 13:
            res = 'overflow'
            break
        cnt += 1
    
    print(f'#{tc} {res}')