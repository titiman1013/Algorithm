import sys; sys.stdin = open('11315.txt', 'r')

dx, dy = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, -1, 1]

def search(board, N):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'o':
                for k in range(8):
                    cnt = 1
                    nx = i + dx[k]
                    ny = j + dy[k]
                    while 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 'o':
                        cnt += 1
                        if cnt >= 5:
                            return 'YES'
                        nx += dx[k]
                        ny += dy[k]
    return 'NO'



for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [input() for _ in range(N)]

    answer = search(board, N)

    print(f'#{tc} {answer}')