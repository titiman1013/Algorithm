import sys; sys.stdin = open('9205.txt', 'r')

from collections import deque

def bfs():
    deq = deque([home])
    while deq:
        x, y = deq.popleft()
        if abs(x - target[0]) + abs(y - target[1]) <= 1000:
            return 'happy'
        else:
            if stores:
                for store in stores:
                    if x == store[0] and y == store[1]: continue
                    if abs(x - store[0]) + abs(y - store[1]) <= 1000:
                        deq.append(store)
                        stores.remove(store)
    return 'sad'
                    



for tc in range(1, int(input()) + 1):
    N = int(input())
    home = list(map(int, input().split()))
    stores = [list(map(int, input().split())) for _ in range(N)]
    target = list(map(int, input().split()))

    answer = bfs()

    print(answer)
    # print(f'{tc} {answer}')