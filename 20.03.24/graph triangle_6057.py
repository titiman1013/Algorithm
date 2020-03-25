import sys; sys.stdin = open("graph triangle.txt", "r")

# 뭐한거?
# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(M)]

#     visit = [0] * (N+1)
#     res = 0
#     for i in range(len(arr)):
#         if visit[arr[i][0]] == 0:
#             stack = []
#             stack.append(arr[i][0])
#             while stack:
#                 x = stack.pop()
#                 visit[x] = 1
#                 for j in range(len(arr)):
#                     if arr[j][0] == x and visit[arr[j][1]] == 0:
#                         stack.append(arr[j][0])
#                     if arr[j][0] == x and visit[arr[j][1]] == 0:
#                         stack.append(arr[j][1])
#             res += 1

#     print(f'#{tc} {res}')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    
    visit = [0] * (N+1)
    res = 0     # 이걸로 삼각형 개수
    for i in range(len(arr)):
        if visit[arr[i][0]] == 0:
            start = arr[i][0]    # 이걸로 출발점
            for j in range(len(arr)):
                if arr[j][0] == start:
                    temp = arr[j][1]
                    for k in range(len(arr)):
                        if arr[k][0] == temp:
                            if arr[k][1] == start:
                                res += 1
                        elif arr[k][1] == temp:
                            if arr[k][0] == start:
                                res += 1
                elif arr[j][1] == start:
                    temp = arr[j][0]
                    for k in range(len(arr)):
                        if arr[k][0] == temp:
                            if arr[k][1] == start:
                                res += 1
                        elif arr[k][1] == temp:
                            if arr[k][0] == start:
                                res += 1

    print(f'#{tc} {res}')