import sys; sys.stdin = open('text1.txt', 'r')

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def move_fireball(x, y, m, s, d):
    for _ in range(s):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N:
            x, y = nx, ny
        else:
            if nx < 0 or nx >= N:
                if nx < 0:
                    x = N + nx
                else:
                    x = nx - N
            if ny < 0 or nx >= N:
                if ny < 0:
                    y = N + ny
                else:
                    y = ny - N

    if bool(arr[x][y]):
        arr[x][y].append([x, y, m, s, d])
    else:
        arr[x][y] = [[x, y, m, s, d]]
    
    return


def sum_fireball(sum_list):
    list_cnt = len(sum_list)
    m = 0
    s = 0
    d = []
    for idx in range(list_cnt):
        m += sum_list[idx][2]
        s += sum_list[idx][3]
        if d % 2:
            d.append(1)
        else:
            d.append(0)
    
    m = m // 5
    if m == 0:
        return [0]
    s = s // list_cnt
    d_check = True
    temp_d = d[0]
    for i in range(1, len(d)):
        if d[i] != temp_d:
            d_check = False
            break
    if d_check == True:
        d = [0, 2, 4, 6]
    else:
        d = [1, 3, 5, 7]

    temp_list = []
    for i in range(4):
        temp_list.append([sum_list[0], sum_list[1], m, s, d[i]])
    return temp_list
    


    # 방향
    # 인접한 행렬 12시부터 시계방향
    # 7 0 1
    # 6   2
    # 5 4 3
for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    # [r, c, m, s, d]
    items = [list(map(int, input().split())) for _ in range(M)]
    arr = [[0] * N for _ in range(N)]

    if K > 0:
        # 처음 시행
        for item in items:
            move_fireball(item[0] - 1, item[1] - 1, item[2], item[3], item[4])
        print(arr)
        move_cnt = 1
        while move_cnt <= K:
            # 움직이기
            for i in range(N):
                for j in range(N):
                    if bool(arr[i][j]):
                        if len(arr[i][j]) >= 2:
                            temp_list = arr[i][j][0]
                            arr[i][j] = 0
                            for k in range(len(temp_list)):
                                move_fireball(temp_list[k][0], temp_list[k][1], temp_list[k][2], temp_list[k][3], temp_list[k][4])
                        else:
                            temp_list = arr[i][j][0]
                            arr[i][j] = 0
                            print(arr)
                            move_fireball(temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4])
            
            # 합치기
            for i in range(N):
                for j in range(N):
                    if len(arr[i][j]) >= 2:
                        arr[i][j] = sum_fireball(arr[i][j])

            move_cnt += 1
    
    res = 0
    for i in range(N):
        for j in range(N):
            if bool(arr[i][j]):
                if len(arr[i][j]) >= 2:
                    for k in range(len(arr[i][j])):
                        res += arr[i][j][k][2]
                else:
                    res += arr[i][j][0][2]
    
    print(f'#{tc} {res}')