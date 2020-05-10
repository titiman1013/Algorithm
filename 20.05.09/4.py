from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(board):
    que = deque()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                que.append((i, j))
                while que:
                    x, y = que.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < len(board) and 0 <= ny < len(board[i]):
                            if board[nx][ny] == 0:
                                if nx == i and ny == j:
                                    continue
                                else:
                                    board[nx][ny] = str(int(board[x][y]) + 1)
                                    que.append((nx, ny))

    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = [board[i][j], 0]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j][0] == 0:
                que.append((i, j))
                while que:
                    # cnt = 0
                    x, y = que.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < len(board) and 0 <= ny < len(board[i]):
                            if int(board[nx][ny][0]) == int(board[x][y][0]) + 1:
                                board[nx][ny][1] = board[x][y][1] + 1
                                if nx == len(board) and ny == len(board[nx]):
                                    print('끝')
                                    que.clear()
                                    break
                                que.append((nx, ny))
                                # cnt += 1
                    # if cnt == 0:
                    #     board[x][y][1] = ''

    print(board)


    answer = 0
    return answer

print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
