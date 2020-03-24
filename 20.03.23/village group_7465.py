import sys; sys.stdin = open('village group.txt', 'r')

# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     arrs = [list(map(int, input().split())) for _ in range(M)]
    
#     temp = 0
#     visit = [0] * (N+1)     # N+1이 올바른 index
#     for arr in arrs:
#         if visit[arr[0]] != 0 and visit[arr[1]] != 0:
#             if visit[arr[0]] == 0 and visit[arr[1]] != 0:
#                 continue
#             if temp - 1 > 0:
#                 temp -= 1
#         elif visit[arr[0]] == 0 and visit[arr[1]] == 0:
#             temp += 1
#         visit[arr[0]] = temp
#         visit[arr[1]] = temp

#     print(f'#{tc} {temp}')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arrs = [list(map(int, input().split())) for _ in range(M)]

    res = 0
    visit = [0] * (N+1)
    for i in range(len(arrs)):
        if visit[arrs[i][0]] == 0:
            stack = []
            stack.append(arrs[0][0])
            while stack:
                x = stack.pop()
                visit[x] = 1
                for i in arrs:
                    