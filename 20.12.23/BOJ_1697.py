import sys; sys.stdin = open('text1.txt', 'r')

# reculsive fail

# def check(pos, sec):
#     global min_sec, K

#     if pos == K:
#         if sec < min_sec:
#             min_sec = sec
#         return

#     if pos > K:
#         check(pos - 1, sec + 1)

#     else:
#         check(pos + 1, sec + 1)
#         check(pos * 2, sec + 1)



# N, K = map(int, input().split())

# min_sec = 100000000
# res = check(N, 0)
# print(min_sec)

# bfs
from collections import deque


def find(N):
    global K

    q = deque()
    q.append(N)
    
    while q:
        x = q.popleft()

        if x == K:
            return arr[x]

        for i in [x + 1, x - 1, x * 2]:
            if 0 <= i < 100001 and arr[i] == 0:
                arr[i] = arr[x] + 1
                q.append(i)



N, K = map(int, input().split())
arr = [0] * 100001
# 예외 존재
# arr[0] = 1
res = find(N)
print(res)