import sys; sys.stdin = open("box change.txt", "r")

#
for tc in range(1, int(input())+1):
    N, Q = map(int, input().split())
    L = []
    for i in range(Q):
        L.append(list(map(int, input().split())))
    L.insert(0, [0, 0])
    
    res = [0] * (N+1)
    for i in range(1, len(L)):
        for j in range(L[i][0], L[i][1]+1):
            res[j] = i
    
    print(f'#{tc}', end=' ')
    for i in range(1, len(res)):
        print(res[i], end=' ')
    print()

# #
# T = int(input())
 
# for t in range(1, T + 1):
#     n, q = map(int, input().split())
#     lst = [0]*n
 
#     for i in range(1, q + 1):
#         l, r = map(int, input().split())
#         for j in range(l-1, r):
#             lst[j] = i
 
#     print('#{} {}'.format(t, ' '.join(list(map(str, lst)))))