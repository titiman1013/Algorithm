import sys; sys.stdin = open('19598.txt', 'r')

# time exceed

# import sys, heapq

# input = sys.stdin.readline

# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     conferences = [tuple(map(int, input().split())) for _ in range(N)]

#     conferences = sorted(conferences, key=lambda x : x[0])

#     answer = 0
#     heap = []
#     for start, end in conferences:
#         if heap:
#             if min(heap) <= start:
#                 heapq.heappop(heap)
#             heapq.heappush(heap, end)
#             if len(heap) > answer:
#                 answer = len(heap)
#         else:
#             heapq.heappush(heap, end)

#     print(answer)




# pypy

# import sys, heapq

# input = sys.stdin.readline

# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     heap = []
#     for _ in range(N):
#         heapq.heappush(heap, tuple(map(int, input().split())))

#     answer = 0
#     rooms = []
#     while heap:
#         start, end = heapq.heappop(heap)
#         if rooms:
#             if min(rooms) <= start:
#                 rooms[rooms.index(min(rooms))] = end
#                 continue
#         rooms.append(end)
#         if len(rooms) > answer:
#             answer = len(rooms)

#     print(answer)



#

import sys, heapq

input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    N = int(input())
    conferences = [tuple(map(int, input().split())) for _ in range(N)]

    conferences.sort()

    answer = 0
    heap = []
    for start, end in conferences:
        if (not heap or heap[0] > start):
            answer += 1
            heapq.heappush(heap, end)
        else:
            heapq.heappop(heap)
            heapq.heappush(heap, end)

    print(answer)