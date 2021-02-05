import sys; sys.stdin = open('2805.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    answer = 0
    for i in range(N // 2):
        for j in range(N // 2 - i, N // 2 + i + 1):
            answer += arr[i][j] + arr[-i - 1][j]
    if N > 1:
        answer += sum(arr[N // 2])
    else:
        answer += arr[0][0]
    print(f'#{tc} {answer}')