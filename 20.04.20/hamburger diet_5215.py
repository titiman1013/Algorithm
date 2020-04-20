import sys; sys.stdin = open("hamburger diet.txt", "r")

# def cal(cnt):
#     global res
#     if cnt == N:
#         score = 0
#         calo = 0
#         for i in range(N):
#             if check[i] == True:
#                 score += arr[i][0]
#                 calo += arr[i][1]
#         if calo <= L:
#             if score > res:
#                 res = score
#         return

#     check[cnt] = False
#     cal(cnt+1)
#     check[cnt] = True
#     cal(cnt+1)



# for tc in range(1, int(input())+1):
#     N, L = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]

#     check = [True] * N
#     res = 0
#     cal(0)
    
#     print(f'#{tc} {res}')


def cal(cnt, score, calo):
    global res
    if cnt == N:
        if calo <= L:
            if score > res:
                res = score
        return

    score_cnt, calo_cnt = arr[cnt]
    cal(cnt+1, score+score_cnt, calo+calo_cnt)
    cal(cnt+1, score, calo)


for tc in range(1, int(input())+1):
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    cal(0, 0, 0)

    print(f'#{tc} {res}')