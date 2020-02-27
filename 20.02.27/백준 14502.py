def wall_create(cnt):
    global result
    if cnt == len(check):
        temp = 0
        wall_list = []
        for i in range(len(check)):
            if check[i] == True:
                temp += 1
                wall_list.append(empty_room_list[i])
                if temp > 3:
                    # print(check)
                    return
        if temp < 3:
            return
        if temp == 3:  # 벽이 3개일 경우만 확인
            print(check)
            clone = []
            for i in range(N):
                clone.append([])
                clone[i] = arr[i][:]
            for wall in wall_list:
                a, b = wall
                clone[a][b] = 1
            for i in range(N):
                for j in range(M):
                    if clone[i][j] == 2:
                        stack = [(i, j)]
                        while stack:
                            x, y = stack.pop()
                            for k in range(4):
                                nx = x + dx[k]
                                ny = y + dy[k]
                                if 0 <= nx < N and 0 <= ny < M:
                                    if clone[nx][ny] == 0:
                                        stack.append((nx, ny))
                                        clone[nx][ny] = 2
                        safety_zone = 0  # 안전구역 개수
                        for i in range(N):
                            for j in range(M):
                                if clone[i][j] == 0:
                                    safety_zone += 1
                        if safety_zone > result:
                            result = safety_zone
            return

    check[cnt] = True
    wall_create(cnt+1)
    check[cnt] = False
    wall_create(cnt+1)




dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]

empty_room_list = []  # 빈 방 리스트
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            empty_room_list.append((i, j))

check = [False] * len(empty_room_list)
result = 0
wall_create(0)
print(result)