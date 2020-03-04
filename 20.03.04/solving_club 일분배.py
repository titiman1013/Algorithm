import sys
sys.stdin = open("일분배.txt", "r")

# 순열 예시
# def f(n, k): # 순열의 n번 원소 결정
#     if n == k:
#         print(p)
#     else:
#         for i in range(k):
#             if used[i] == 0: #i번 원소가 사용되지 않았으면
#                 used[i] = 1 # 사용함 표시
#                 p[n] = A[i]
#                 f(n+1, k) # n+1 원소 결정
#                 used[i] = 0 # 다른자리에서 사용하도록 풀어줌

# A = [1,2,3,4,5]
# used = [0] * 5
# p = [0] * 5
# f(0, 5)

def check(n, k, s):
    global maxV
    if s <= maxV: # 성공확률이 같거나 작으면
        return
    if n == k:
        if maxV < s:
            maxV = s
    else:
        for i in range(k):
            if used[i] == 0:
                used[i] = 1
                check(n+1, k, s*(arr[n][i]/100)) # n번까지의 성공 확률 계싼
                used[i] = 0


T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    res = [0] * N
    used = [0] * N
    maxV = 0
    check(0, N, 1)
    maxV *= 100
    maxV = '%.6f' % maxV
    print(f'#{t+1} {maxV}')