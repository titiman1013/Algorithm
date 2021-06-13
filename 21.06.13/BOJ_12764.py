import sys; sys.stdin = open('12764.txt', 'r')

import sys, heapq

input = sys.stdin.readline

N = int(input())
people = [tuple(map(int, input().split())) for _ in range(N)]

people.sort()

heap = []
cnt = 0
empty_seat = []
use_seat_num = [0] * (N + 1)
using = [False] * (N + 1)
for start, end in people:
    if (not heap or heap[0][0] > start):
        if empty_seat:
            seat_num = heapq.heappop(empty_seat)
            use_seat_num[seat_num] += 1
            heapq.heappush(heap, (end, seat_num))
        else:
            cnt += 1
            use_seat_num[cnt] += 1
            using[cnt] = True
            heapq.heappush(heap, (end, cnt))
    else:
        while heap[0][0] < start:
            seat_num = heapq.heappop(heap)[1]
            heapq.heappush(empty_seat, seat_num)
            if len(heap) == 0: break
        min_seat_num = heapq.heappop(empty_seat)
        use_seat_num[min_seat_num] += 1
        heapq.heappush(heap, (end, min_seat_num))

answer = using.count(True)
print(answer)

for use_seat in use_seat_num[1:]:
    if use_seat:
        print(use_seat, end=' ')
    else: break