import sys; sys.stdin = open('16724.txt', 'r')

# union-find

import sys


input = sys.stdin.readline
move = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0),
}

def find(x):
    if parent[x] == x: return x

    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x, y = find(x), find(y)

    if x == y: return False

    if rank[x] < rank[y]:
        x, y = y, x

    parent[y] = x

    if rank[x] == rank[y]:
        rank[x] += 1
    return True



N, M = map(int, input().split())
board = list(input().rstrip('\n') for _ in range(N))

parent = [i for i in range(N * M)]
rank = [1] * (N * M)

for idx in range(N * M):
    x, y = idx // M, idx % M
    dx, dy = move.get(board[x][y])
    nx, ny = x + dx, y + dy
    if 0 <= nx * M + ny < N * M:
        union(idx, nx * M + ny)

answer = len(set(find(val) for val in range(N * M)))
print(answer)




# # 

# import sys


# input = sys.stdin.readline
# dir = {
#     'L': (0, -1),
#     'R': (0, 1),
#     'U': (-1, 0),
#     'D': (1, 0),
# }

# def move(x, y, group_num):
#     dx, dy = dir[board[x][y]]
#     nx, ny = x + dx, y + dy
    



# N, M = map(int, input().split())
# board = list(input().rstrip('\n') for _ in range(N))

# answer = 0
# cnt = 0
# for i in range(N):
#     for j in range(M):
#         cnt += 1
#         answer += move(i, j, cnt)

# print(answer)