import sys; sys.stdin = open('subscriber war.txt', 'r', encoding="UTF-8")

for tc in range(1, int(input())+1):
    N, A, B = map(int, input().split())

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