import sys; sys.stdin = open('4615.txt', 'r')

dx, dy = [-1, 1, 0, 0, -1, 1, -1, 1], [0, 0, -1, 1, -1, -1, 1, 1]

def initial_set(N):
    board = [[0] * (N + 1) for _ in range(N + 1)]
    mid = N // 2
    board[mid][mid] = 2
    board[mid][mid + 1] = 1
    board[mid + 1][mid] = 1
    board[mid + 1][mid + 1] = 2
    return board


def go(board, dx, dy, nx, ny, color, N, k):
    move_points = [(nx, ny)]
    while board[nx][ny] != 0 and board[nx][ny] != color:
        nx += dx[k]
        ny += dy[k]
        move_points.append((nx, ny))
        if nx < 0 or nx > N or ny < 0 or ny > N:
            return False
    if board[nx][ny] == color:
        for i, j in move_points:
            board[i][j] = color
    return board


def check(board, N):
    answer = [0, 0]
    for i in range(N + 1):
        for j in range(N + 1):
            if board[i][j] == 1:
                answer[0] += 1
            elif board[i][j] == 2:
                answer[1] += 1
    return answer



for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    plays = list(list(map(int, input().split())) for _ in range(M))

    board = initial_set(N)
    for y, x, color in plays:
        board[x][y] = color
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N + 1 and 0 <= ny < N + 1:
                tmp = go(board, dx, dy, nx, ny, color, N, k)
                if tmp:
                    board = tmp
    
    answer = check(board, N)

    print(f'#{tc} {answer[0]} {answer[1]}')