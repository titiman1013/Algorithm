import sys; sys.stdin = open('tell vertical line.txt', 'r')

for tc in range(1, int(input())+1):
    arr = list(input() for _ in range(5))

    max_length = 0
    for i in range(5):
        if len(arr[i]) > max_length:
            max_length = len(arr[i])

    res = ''
    for i in range(max_length):
        for j in range(5):
            if len(arr[j]) > i:
                res += arr[j][i]
            else:
                continue

    print(f'#{tc} {res}')