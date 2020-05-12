import sys; sys.stdin = open('gear.txt', 'r')
from collections import deque

# def check(number, direction):
#     if arr[number-1][2] != arr[number][6]:
        
#     if arr[number-1][6] != arr[number-2][2]:
#         pass

for tc in range(1, int(input())+1):
    arr = [list(map(int, list(input()))) for _ in range(4)]
    # (1번 2, 2번 6), (2번 2, 3번 6), (3번 2, 4번 6)
    K = int(input())
    # 회전 횟수
    ways = [list(map(int, input().split())) for _ in range(K)]
    # 톱니바퀴번호, 회전방향

    # que = deque()
    # for i in range(len(arr)):
    #     que.append(arr[i])

    for way in ways:
        number, direction = way
        temp_list = []
        for i in range(len(arr)):
            temp_list.append((arr[i][2], arr[i][6]))
        
        # 뒤로갈때
        direction_back = direction
        for j in range(number-1, 3):
            if temp_list[j][0] != temp_list[j+1][1]:
                direction_back = -direction_back
                if direction_back == -1:
                    arr[j+1].append(arr[j+1].pop(0))
                else:
                    arr[j+1].insert(0, arr[j+1].pop())
            else:
                break

        # 앞으로
        direction_forward = direction
        for j in range(number-1, 0, -1):
            if temp_list[j][1] != temp_list[j-1][0]:
                direction_forward = -direction_forward
                if direction_forward == -1:
                    arr[j-1].append(arr[j-1].pop(0))
                else:
                    arr[j-1].insert(0, arr[j-1].pop())
            else:
                break

        # 회전시작톱니
        if direction == -1:
            arr[number-1].append(arr[number-1].pop(0))
        else:
            arr[number-1].insert(0, arr[number-1].pop())
        # print(arr)

    res = 0
    if arr[0][0] == 1:
        res += 1
    if arr[1][0] == 1:
        res += 2
    if arr[2][0] == 1:
        res += 4
    if arr[3][0] == 1:
        res += 8

    print(f'#{tc} {res}')