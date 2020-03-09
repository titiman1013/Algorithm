import sys; sys.stdin = open('two numbers.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # A와 B의 수열의 길이에 주의
    if N > M:
        A, B = B, A
        N, M = M, N  # A: 짧은 수열, B: 긴 수열

    # 길이가 N인 구간의 모든 시작 위치에 대해
    Max = -10000000
    for i in range(M - N + 1):
        S = 0
        for j in range(N):
            S += (A[j] * B[i + j])

        Max = max(Max, S)
    print('#{} {}'.format(tc, Max))