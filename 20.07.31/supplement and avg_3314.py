import sys; sys.stdin = open('supplement and avg.txt', 'r')

for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))

    res = 0
    for i in range(len(arr)):
        if arr[i] < 40:
            res += 40
        else:
            res += arr[i]

    print(f'#{tc} {res//5}')