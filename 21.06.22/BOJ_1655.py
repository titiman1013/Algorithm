import sys; sys.stdin = open('1655.txt', 'r')

import sys, heapq

input = sys.stdin.readline

N = int(input())
nums = list(int(input()) for _ in range(N))

low_heap, high_heap = [], []
for num in nums:
    if low_heap or high_heap:
        if len(low_heap) == len(high_heap):
            heapq.heappush(low_heap, -num)
        else:
            heapq.heappush(high_heap, num)

        if low_heap and high_heap and -low_heap[0] > high_heap[0]:
            low, high = heapq.heappop(low_heap), heapq.heappop(high_heap)
            heapq.heappush(low_heap, -high)
            heapq.heappush(high_heap, -low)

    else:
        heapq.heappush(low_heap, -num)

    print(-low_heap[0])