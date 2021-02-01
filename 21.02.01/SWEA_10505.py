import sys; sys.stdin = open('10505.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    answer = 0
    avg = sum(arr) // N + 1
    for i in range(N):
        if arr[i] < avg:
            answer += 1
    print(f'#{tc} {answer}')