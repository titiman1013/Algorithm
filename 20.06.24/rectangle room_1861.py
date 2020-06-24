import sys; sys.stdin = open('rectangle room.txt', 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
 
for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    res_list = []
 
    for i in range(N):
        for j in range(N):
            x = i
            y = j
            cnt = 1
            nx = i
            ny = j
            while True:
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if arr[x][y] + 1 == arr[nx][ny]:
                            x = nx
                            y = ny
                            cnt += 1
                            break
                else: 
                    break   
            if cnt > result:
                result = cnt
                if res_list:
                    res_list.clear()
                    res_list.append(arr[i][j])
                else:
                    res_list.append(arr[i][j])
            elif cnt == result:
                if res_list:
                    if res_list[0] > arr[i][j]:
                        res_list.clear()
                        res_list.append(arr[i][j])
                else:
                    res_list.append(arr[i][j])
 
    print(f'#{tc} {res_list[0]} {result}')
