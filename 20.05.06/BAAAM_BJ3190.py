import sys; sys.stdin =open('BAAAM.txt', 'r')

#
# for tc in range(1, int(input())+1):
#     N = int(input())
#     K = int(input())
#     apples = [list(map(int, input().split())) for _ in range(K)]
#     L = int(input())
#     direction = [list(input().split()) for _ in range(L)]
#     # arr = [[0] * N for _ in range(N)]

#     x = 1
#     y = 1
#     head = [1, 1]
#     tail = [1, 1]
#     time = 0
#     head_direction = 'right'
#     tail_direction = 'right'
#     turn = []
#     for i in range(L):
#         turn.append((i, int(direction[i][0])))
#     turn_direction, turn_time = turn.pop(0)
#     tail_turn = []
#     tail_turn_direction = []
#     while (0 <= x < N + 1 and 0 <= y < N + 1) or head == tail:
#         time += 1
#         if head_direction == 'right':
#             head[1] += 1
#             y += 1
#         elif head_direction == 'left':
#             head[1] -= 1
#             y -= 1
#         elif head_direction == 'up':
#             head[0] -= 1
#             x -= 1
#         else:
#             head[0] += 1
#             x += 1
        
#         if head in apples:
#             if tail_direction == 'right':
#                 tail[1] += 1
#             elif tail_direction == 'left':
#                 tail[1] -= 1
#             elif tail_direction == 'up':
#                 tail[0] -= 1
#             else:
#                 tail[0] += 1
        
#         if time == turn_time:
#             if direction[turn_direction][1] == 'L':
#                 if head_direction == 'right':
#                     head_direction = 'up'
#                 elif head_direction == 'left':
#                     head_direction = 'down'
#                 elif head_direction == 'up':
#                     head_direction = 'left'
#                 else:
#                     head_direction = 'right'
#             else:
#                 if head_direction == 'right':
#                     head_direction = 'down'
#                 elif head_direction == 'left':
#                     head_direction = 'up'
#                 elif head_direction == 'up':
#                     head_direction = 'right'
#                 else:
#                     head_direction = 'left'
#             tail_turn.append((x, y))
#             tail_turn_direction.append(direction[i][1])
#             if turn:
#                 turn_direction, turn_time = turn.pop(0)
        
#         if tail in tail_turn:
#             if tail_turn_direction.pop(0) == 'L':
#                 if tail_direction == 'right':
#                     tail_direction = 'up'
#                 elif tail_direction == 'left':
#                     tail_direction = 'down'
#                 elif tail_direction == 'up':
#                     tail_direction = 'left'
#                 else:
#                     tail_direction = 'right'
#             else:
#                 if tail_direction == 'right':
#                     tail_direction = 'down'
#                 elif tail_direction == 'left':
#                     tail_direction = 'up'
#                 elif tail_direction == 'up':
#                     tail_direction = 'right'
#                 else:
#                     tail_direction = 'left'                
    
#     print(f'#{tc} {time}')


#
for tc in range(1, int(input())+1):
    N = int(input())
    K = int(input())
    arr = [[0] * N for _ in range(N)]
    apples = [list(map(int, input().split())) for _ in range(K)]
    # 사과칸은 2로 표시
    for i in range(len(apples)):
        arr[apples[i][0]-1][apples[i][1]-1] = 2
    # print(arr)
    L = int(input())
    directions = [list(input().split()) for _ in range(L)]
    # print(directions)
    
    x, y = 0, 0
    res = 0
    tail_list = [[0, 0]]
    tail = tail_list.pop(0)
    dx, dy = 0, 1
    turn_time, head_direction = directions.pop(0)
    while 0 <= x < N and 0 <= y < N:
        res += 1

        if res == 1:
            arr[x][y] = 1

        # 머리 이동
        nx, ny = x + dx, y + dy
        if not (0 <= nx < N and 0 <= ny < N):
            break
        # 몸통이면 끝
        if arr[nx][ny] == 1:
            break
        else:
            # 사과 만나면
            tail_list.append((nx, ny))
            if arr[nx][ny] != 2:
                arr[tail[0]][tail[1]] = 0
                tail = tail_list.pop(0)
            arr[nx][ny] = 1
            x = nx
            y = ny
        
        # 머리의 방향전환
        if res == int(turn_time):
            if head_direction == 'L':
                if (dx == -1 or dx == 1) and dy == 0:
                    dx, dy = dy, dx
                else:
                    dx, dy = -dy, dx
            else:
                if dx == 0 and (dy == 1 or dy == -1):
                    dx, dy = dy, dx
                else:
                    dx, dy = dy, -dx
            if directions:
                turn_time, head_direction = directions.pop(0)
    
    print(f'#{tc} {res}')