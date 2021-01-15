import sys; sys.stdin = open('text1.txt', 'r')

# memory exceed

# from collections import deque

# def bfs():
#     deq = deque()
#     deq.append(1)
#     while deq:
#         x = deq.popleft()
#         for i in range(2, N + 1):
#             if arr[x][i] and parent[i] == 0:
#                 deq.append(i)
#                 parent[i] = x



# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     arr = [[0] * (N + 1) for _ in range(N + 1)]
#     for _ in range(N - 1):
#         x, y = map(int, input().split())
#         arr[x][y] = 1
#         arr[y][x] = 1
#     parent = [0] * (N + 1)

#     bfs()
#     for i in range(2, len(parent)):
#         print(parent[i])


# time error

# from collections import defaultdict

# def bfs():
#     s = [1]
#     for x, y in arr:
#         if x == 1:
#             dic[1].add(y)
#         elif y == 1:
#             dic[1].add(x)

#     while s:
#         x = s.pop()
#         x_lst = dic.get(x)
#         for i in x_lst:
#             if parents[i] == 0:
#                 for p, q in arr:
#                     if p == i:
#                         dic[i].add(q)
#                     elif q == i:
#                         dic[i].add(p)
#                 parents[i] = x
#                 s.append(i)



# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N - 1)]
#     dic = defaultdict(set)
#     parents = [0] * (N + 1)
    
#     bfs()
#     for i in range(2, len(parents)):
#         print(parents[i])



# solve3

# from collections import defaultdict, deque

# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     dic = defaultdict(list)
#     for _ in range(N - 1):
#         x, y = map(int, input().split())
#         dic[x].append(y)
#         dic[y].append(x)
#     parents = [0] * (N + 1)

#     deq = deque([1])
#     parents[1] = -1
#     while deq:
#         x = deq.popleft()
#         for y in dic.get(x):
#             if parents[y] == 0:
#                 parents[y] = x
#                 deq.append(y)
    
#     for i in range(2, len(parents)):
#         print(parents[i])



# sys.readline

from collections import defaultdict, deque
import sys

input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    N = int(input())
    dic = defaultdict(list)
    for _ in range(N - 1):
        x, y = map(int, input().split())
        dic[x].append(y)
        dic[y].append(x)
    parents = [0] * (N + 1)

    deq = deque([1])
    parents[1] = -1
    while deq:
        x = deq.popleft()
        for y in dic.get(x):
            if parents[y] == 0:
                parents[y] = x
                deq.append(y)
    
    for i in range(2, len(parents)):
        print(parents[i])