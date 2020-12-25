import sys; sys.stdin = open('text1.txt', 'r')
from collections import deque


def create(N):
    q = deque()
    for i in range(N):
        q.append(i)
    return q


def shuffle():
    while len(arr) != 1:
        x = arr.popleft()
        temp = arr.popleft()
        arr.append(temp)
    return arr[0] + 1


N = int(input())
arr = create(N)
res = shuffle()
print(res)