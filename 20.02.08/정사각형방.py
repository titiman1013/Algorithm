import sys
sys.stdin = open("정사각형방.txt", "r")

T = int(input())
for t in range(T):
    print(f'#{t+1}', end = ' ')
    N = int(input())
    arr = []
    for n in range(N): # 2차원배열 생성
        arr.append(list(map(int, input().split())))
    start = []
    result = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            a = arr[i][j]
            x = i
            y = j
            while True:
            # while arr[x][y] + 1 == arr[x][y-1] or arr[x][y] + 1 == arr[x-1][y] or arr[x][y] + 1 == arr[x][y+1] or arr[x][y] + 1 == arr[x+1][y]: 

                while x > 0: # 올라가기
                    if arr[x][y] + 1 == arr[x-1][y]:
                        cnt += 1
                        x -= 1
                    else:
                        break
                while y > 0: # 왼쪽
                    if arr[x][y] + 1 == arr[x][y-1]:
                        cnt += 1
                        y -= 1
                    else:
                        break
                while y < N-1: # 오른쪽
                    if arr[x][y] + 1 == arr[x][y+1]:
                        cnt += 1
                        y += 1
                    else:
                        break
                while x < N-1: # 내려가기
                    if arr[x][y] + 1 == arr[x+1][y]:
                        cnt += 1
                        x += 1
                    else:
                        break
                if cnt >= 200:
                    cnt = 2199
                break
            if cnt > result:
                start.clear()
                start.append(a)
                # start.append(x)
                # start.append(y)
                result = cnt
            elif cnt == result:
                start.append(a)
    if result == 2199:
        start.clear()
        start.append(8225)
    print(f'{min(start)}', end = ' ')
    print(f'{result+1}')