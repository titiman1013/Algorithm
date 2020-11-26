import sys; sys.stdin = open('text1.txt', 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_airCleaner():
    airCleaner = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] == -1:
                airCleaner.append((i, j))
                if len(airCleaner) == 2:
                    return airCleaner



def dust_diffusion():
    next_list = [[0] * C for _ in range(R)]
    next_list[airCleaner[0][0]][airCleaner[0][1]] = -1
    next_list[airCleaner[1][0]][airCleaner[1][1]] = -1
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                dust_cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < R and 0 <= ny < C:
                        if arr[nx][ny] != -1:
                            next_list[nx][ny] += (arr[i][j] // 5)
                            dust_cnt += 1
                next_list[i][j] = arr[i][j] - ((arr[i][j] // 5) * dust_cnt)
                #            arr[nx][ny] += (arr[i][j] // 5)
                #            dust_cnt += 1
                #arr[i][j] -= (arr[i][j] // 5) * dust_cnt
    return next_list



def wind():
    for idx, position in enumerate(airCleaner):
        x, y = position[0], position[1]
        direction = 0
        if idx == 0:
            while direction < 4:
                x, y, temp = goRight(x, y)
                direction += 1
                x, y, temp = goTop(x, y, temp)
                direction += 1
                x, y, temp = goLeft(x, y, temp)
                direction += 1
                x, y, temp = goBottom(x, y, temp)
                direction += 1
        else:
            while direction < 4:
                x, y, temp = goRight(x, y)
                direction += 1
                x, y, temp = goBottom(x, y, temp)
                direction += 1
                x, y, temp = goLeft(x, y, temp)
                direction += 1
                x, y, temp = goTop(x, y, temp)
                direction += 1
    return "Wind_Success"


def goTop(x, y, pre):
    temp = pre
    while True:
        x -= 1
        # 벽일때
        if x == -1:
            return x + 1, y, temp

        nex = arr[x][y]
        arr[x][y] = temp
        temp = nex


def goBottom(x, y, pre):
    temp = pre
    while True:
        x += 1
        if x == R - 1 or x == -1:
            return x - 1, y, temp
        
        nex = arr[x][y]
        arr[x][y] = temp
        temp = nex


def goLeft(x, y, pre):
    temp = pre
    while True:
        y -= 1
        if y == -1:
            return x, y + 1, temp

        nex = arr[x][y]
        arr[x][y] = temp
        temp = nex


def goRight(x, y):
    # 먼지 밀면서 가져온 값
    now = 0
    while True:
        # 한칸 오른쪽으로 옮기고 시작
        y += 1
        # 만약 벽에 닿으면 return
        if y == C - 1:
            return x, y - 1, nex

        # if temp:
        #     nex = arr[x][y]
        #     arr[x][y] = temp
        #     temp = nex
        # else:

        # 현재 내 위치 값
        nex = arr[x][y]
        arr[x][y] = now
        now = nex
        # # 다음 칸 값
        # nex = arr[x][y + 1]
        # arr[x][y + 1] = now
        # temp = nex



def count_dust():
    cnt = 0
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                cnt += arr[i][j]
    return cnt



for tc in range(1, int(input()) + 1):
    R, C, T = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(R)]
    
    airCleaner = find_airCleaner()
    for time in range(T):
        arr = dust_diffusion()
        # wind()
        for i in arr:
            print(i)
        print()
        
    res = count_dust()
    print(f'{tc} {res}')