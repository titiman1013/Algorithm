import sys; sys.stdin = open('1005.txt', 'r')

# false

import sys
from collections import deque

input = sys.stdin.readline

def topo_sort():
    deq = deque()
    output = []
    for i in range(1, N + 1):
        if degrees[i] == 0:
            deq.append(i)
            output.append(i)

    answer = 0
    while deq:
        max_time = 0
        tmp_deq = deque()
        for current in deq:
            if current == target: 
                answer += times[current]
                return answer
            for next in graphs.get(current):
                degrees[next] -= 1
                max_time = max(max_time, times[current])
                if degrees[next] == 0:
                    tmp_deq.append(next)
                    output.append(next)
        deq = tmp_deq
        answer += max_time
    
    return answer



for _ in range(1, int(input()) + 1):
    for tc in range(1, int(input()) + 1):
        N, K = map(int, input().split())
        times = [0] + list(map(int, input().split()))
        orders = [tuple(map(int, input().split())) for _ in range(K)]
        target = int(input())

        graphs = {i: [] for i in range(N + 1)}
        degrees = [0 for _ in range(N + 1)]
        for pre, post in orders:
            graphs[pre].append(post)
            degrees[post] += 1

        print(topo_sort())