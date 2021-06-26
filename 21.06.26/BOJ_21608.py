import sys; sys.stdin = open('21608.txt', 'r')

import sys


input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for tc in range(1, int(input()) + 1):
    N = int(input())
    students = [list(map(int, input().split())) for _ in range(N ** 2)]

    arr = [[0] * N for _ in range(N)]
    prefer_dict = dict()
    for student in students:
        num, prefers = student[0], student[1:]
        prefer_dict[num] = prefers
        
        prefer_cnt = 0
        empty_cnt = 0
        seat = [float('inf'), float('inf')]
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 0:
                    tmp_prefer, tmp_empty = 0, 0
                    for k in range(4):
                        nx, ny = i + dx[k], j + dy[k]
                        if 0 <= nx < N and 0 <= ny < N:
                            if arr[nx][ny] in prefers:
                                tmp_prefer += 1
                            elif arr[nx][ny] == 0:
                                tmp_empty += 1
                    
                    if prefer_cnt > tmp_prefer:
                        continue
                    elif prefer_cnt == tmp_prefer:
                        if empty_cnt > tmp_empty:
                            continue
                        elif empty_cnt == tmp_empty:
                            if seat[0] < i:
                                continue
                            elif seat[0] == i:
                                if seat[1] < j:
                                    continue
                    prefer_cnt = tmp_prefer
                    empty_cnt = tmp_empty
                    seat = [i, j]
        
        arr[seat[0]][seat[1]] = num
        
    answer = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    if arr[nx][ny] in prefer_dict[arr[i][j]]:
                        cnt += 1
            if cnt > 0:
                answer += 10 ** (cnt - 1)
    
    print(answer)