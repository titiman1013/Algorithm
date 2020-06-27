import sys; sys.stdin = open('ladder.txt', 'r')

for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    start = []
    for i in range(100):
        if arr[0][i] == 1:
            start.append(i)

    res = 100000     # start point
    for now in start:
        length = 0
        for i in range(1, 100):
            if arr[i][now-1] == 1:
                while arr[i][now-1] == 1:
                    if 0 <= now - 1 < 100:
                        now = now - 1
                        length += 1    
            elif arr[i][now+1] == 1:
                while arr[i][now+1] == 1:
                    if 0 <= now + 1 < 100:
                        now = now + 1
                        length += 1
        if length < res:
            res = length

    print(f'#{tc} {res}')