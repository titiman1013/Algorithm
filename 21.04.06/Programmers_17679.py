def search(m, n, board):
    same_blocks = set()
    for i in range(m - 1):
        for j in range(n - 1):
            if board[i][j].isnumeric(): continue
            if len(set(board[i][j:j + 2] + board[i + 1][j:j + 2])) == 1:
                for p in range(2):
                    for q in range(2):
                        same_blocks.add((i + p, j + q))
    return same_blocks


def boom(board, same_blocks):
    for i, j in same_blocks:
        board[i][j] = '0'
    return board


def down(m, n, board):
    for j in range(n):
        for i in range(m - 1, 0, -1):
            if board[i][j] == '0':
                x = 1
                while i - x >= 0:
                    if board[i - x][j] == '0':
                        if i - (x + 1) < 0: break 
                        x += 1
                    else: break
                board[i][j] = board[i - x][j]
                board[i - x][j] = '0'
    return board


def solution(m, n, board):
    answer = 0

    board = [list(map(str, tmp_lst)) for tmp_lst in board]
    while True:
        same_blocks = search(m, n, board)
        if len(same_blocks) == 0:
            break
        answer += len(same_blocks)
        board = boom(board, same_blocks)
        board = down(m, n, board)

    return answer




print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))

# answer
# 14
# 15