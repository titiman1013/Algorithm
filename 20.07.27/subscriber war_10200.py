import sys; sys.stdin = open('subscriber war.txt', 'r', encoding="UTF-8")

for tc in range(1, int(input())+1):
    N_temp, A_temp, B_temp = input().split()
    if N_temp == '\u200b\u200b\u200b\u200b\u200b\u200b\u200b100':
        N = 100
    else:
        N = int(N_temp)
    if A_temp == '\u200b\u200b\u200b\u200b\u200b\u200b\u200b100':
        A = 100
    else:
        A = int(A_temp)
    if B_temp == '\u200b\u200b\u200b\u200b\u200b\u200b\u200b100':
        B = 100
    else:
        B = int(B_temp)

    max_sub = 0
    min_sub = 0
    max_sub = min(A, B)
    if max(A, B) > N // 2:
        min_sub = max_sub - (N - max(A, B))
    else:
        min_sub = 0

    if min_sub < 0:
        min_sub = 0

    print(f'#{tc} {max_sub} {min_sub}')

# 인코딩 문제때문에 test case3 이 실행되지 않음