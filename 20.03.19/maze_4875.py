import sys; sys.stdin = open('maze.txt', 'r')

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# for tc in range(1, int(input())+1):
#     N = int(input())
#     arr = [list(map(int, list(input()))) for _ in range(N)]
    
#     stack = []
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 2:
#                 stack.append((i, j))
#                 break
    
#     result = 0
#     while stack:
#         x, y = stack.pop()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < N and 0 <= ny < N:
#                 if arr[nx][ny] == 3:
#                     result = 1
#                 elif arr[nx][ny] == 0:
#                     arr[nx][ny] = 1
#                     stack.append((nx, ny))

#     print(f'#{tc} {result}')


#
def f(sRow, sCol, N):
    dRow = [0, 1, 0, -1]
    dCol = [1, 0, -1, 0]
    s = []
    s.append([sRow, sCol])      # 입구로 이동
    maze[sRow][sCol] = 1        # 방문 표시
    while s:        # 스택에 좌표가 남아있으면
        row, col = s.pop()      # 갈 수 있는 위치
        if maze[row][col] == 3:     # 출구인경우 1반환
            return 1
        for i in range(4):      # 주변 좌표 계산
            nRow = row + dRow[i]
            nCol = col + dCol[i]
            if 0 <= nRow < N and 0 <= nCol < N:     # 미로 내부
                if maze[nRow][nCol] != 1:   # 갈 수 있는 곳 저장
                    s.append([nRow, nCol])
                    maze[row][col] = 1
    return 0            # 출구에 가지 못하고 끝날 때




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [[int(x) for x in input()] for _ in range(N)]    # 미로를 저장
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sRow, sCol = i, j       # 출발 row index
    print('#{} {}'.format(tc, f(sRow, sCol, N)))