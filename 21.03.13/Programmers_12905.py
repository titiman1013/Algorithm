from itertools import chain

def solution(board):
    answer = 0

    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            if board[i][j]:
                board[i][j] = min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1
    
    answer = max(chain(*board)) ** 2

    return answer




print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0,0,1,1],[1,1,1,1]]))

# answer
# 9
# 4