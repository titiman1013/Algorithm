import sys; sys.stdin = open("paper attach.txt", "r")

# # 재귀
# def f(n):
#     if n < 2:
#         return 1
#     else:
#         return f(n-1) + 2 * f(n-2)




# for tc in range(1, int(input())+1):
#     N = int(input()) // 10      # 10의 배수를 종이의 폭으로 나눔
#     print('#{} {}'.format(tc, f(N)))


# 단순반복
F = [0] * 31
F[1] = 1
F[2] = 3        # f(1) = 1, f(2) = 3
for i in range(3, 31):  # 문제의 조건에서 f(30)까지 필요
    F[i] = F[i-1] + 2 * F[i-2]  # 점화식 f(n) = f(n-1) + 2 * f(n-2)


for tc in range(1, int(input())+1):
    N = int(input()) // 10      # 10의 배수를 종이의 폭으로 나눔
    print('#{} {}'.format(tc, F[N]))