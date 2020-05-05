import sys; sys.stdin = open('10.txt', 'r')
import copy 
from itertools import combinations
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check():
    # global res
    garden = [[[0, 0] for i in range(M)] for j in range(N)]
    # 왼쪽이 배양액색 오른쪽이 전이된 턴
    que = deque()

    for i, j in pick_green:
        garden[i][j][0] = 'green'
        que.append((i, j))
    for i, j in pick_red:
        garden[i][j][0] = 'red'
        que.append((i, j))
    for i, j in water_list:
        garden[i][j][0] = 'water'
    # print(garden)

    flower = 0
    while que:
        x, y = que.popleft()
        if garden[x][y][0] == 'flower':
            continue
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                # if garden[nx][ny][0] == 'water':
                #     continue
                if garden[nx][ny][0] == 0:
                    garden[nx][ny][0] = garden[x][y][0]
                    garden[nx][ny][1] = garden[x][y][1] + 1
                    que.append((nx, ny))
                elif garden[nx][ny][0] == 'green':
                    if garden[x][y][0] == 'red' and garden[x][y][1] + 1 == garden[nx][ny][1]:
                        garden[nx][ny][0] = 'flower'
                        flower += 1
                        # print((nx, ny))
                elif garden[nx][ny][0] == 'red':
                    if garden[x][y][0] == 'green' and garden[x][y][1] + 1 == garden[nx][ny][1]:
                        garden[nx][ny][0] = 'flower'
                        flower += 1
                        # print((nx, ny))
    # print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    # if res < flower:
    #     print(garden)
    return flower



for tc in range(1, int(input())+1):
    N, M, G, R = map(int, input().split())
    # N 은 행, M 은 열, G는 초록배양액, R은 빨간배양액
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 0은 호수, 1은 배양액 뿌릴수없는땅, 2는 있는땅
    
    pick_list = []
    water_list = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                pick_list.append((i, j))
            elif arr[i][j] == 0:
                water_list.append((i, j))
    
    res = 0
    for pick in combinations(pick_list, G+R):
        # print(pick)
        for green in combinations(range(G+R), G):
            pick_green = []
            pick_red = []
            for i in range(R+G):
                if i in green:
                    pick_green.append(pick[i])
                else:
                    pick_red.append(pick[i])
            # print(pick_green, pick_red)
            temp = check()
            # print(temp)
            if res < temp:
                # print(res, temp)
                res = temp 
    # print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    print(f'#{tc} {res}')