import sys; sys.stdin = open('binary search.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))


    res = 0
    for b in list_b:
        # if b > list_a[-1]: break
        if b in list_a:
            l = 0
            r = len(list_a) - 1
            m = (l + r) // 2
            check = -1
            while l <= r:
                if list_a[m] == b:
                    res += 1; break
                elif list_a[l] <= b < list_a[m]:
                    r = m - 1
                    m = (l + r) // 2
                    if check != -1:
                        if check == 0: break
                        else: check = 0
                    else:
                        check = 0
                elif list_a[m] < b <= list_a[r]:
                    l = m + 1
                    m = (l + r) // 2
                    if check != -1:
                        if check == 1: break
                        else: check = 1
                    else:
                        check = 1
    
    print(f'#{tc} {res}')





# #
# T=int(input())
# def find(ar,num):
#     left =0
#     right = N-1
#     flag = -1
#     while True:
#         m = (left+right)//2
#         if num == ar[m]:
#             return 1
#         else:
#             if flag == -1:
#                 if num>ar[m]:
#                     flag = True
#                     left = m +1
#                 else:
#                     flag = False
#                     right = m-1
#             else:
#                 if num>ar[m]:
#                     if flag:
#                         return 0
#                     else:
#                         flag = True
#                         left = m +1
#                 else:
#                     if flag:
#                         flag = False
#                         right = m -1
#                     else:
#                         return 0
# for tc in range(1,T+1):
#     N,M=map(int,input().split())
#     list_a=list(map(int,input().split()))
#     list_b=list(map(int,input().split()))
#     list_a.sort()
#     cnt=0
#     for i in range(M):
#         if list_b[i] in list_a:
#             cnt += find(list_a,list_b[i])
#     print('#{} {}'.format(tc,cnt))