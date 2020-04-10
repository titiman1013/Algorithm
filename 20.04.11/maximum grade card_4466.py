import sys; sys.stdin = open("maximum grade card.txt", "r")

# # 1
# for tc in range(1, int(input())+1):
#     N, K = map(int, input().split())
#     scores = list(map(int, input().split()))

#     scores.sort()
#     res = 0
#     for i in range(N-1, N-1-K, -1):
#         res += scores[i]
#     print(f'#{tc} {res}')



# 2
def max_(cnt):
    global res
    if cnt == N:
        temp = 0
        c = 0
        for i in range(N):
            if check[i] == True:
                temp += scores[i]
                c += 1 
        if temp > res and c == K:
            res = temp
        return

    check[cnt] = True
    max_(cnt+1)
    check[cnt] = False
    max_(cnt+1)

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))

    check = [False] * N
    res = 0
    max_(0)

    print(f'#{tc} {res}')