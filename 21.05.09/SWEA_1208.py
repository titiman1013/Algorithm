import sys; sys.stdin = open('1208.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):
        if arr.count(max(arr)) >= len(arr) - 1: break
        arr[arr.index(max(arr))] -= 1
        arr[arr.index(min(arr))] += 1

    answer = max(arr) - min(arr)

    print(f'#{tc} {answer}')