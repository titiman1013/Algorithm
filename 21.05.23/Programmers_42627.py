import heapq

def solution(jobs):
    answer = 0

    N = len(jobs)
    heap = []
    time, last, cnt = 0, -1, 0
    while cnt < N:
        for start, during in jobs:
            if last < start <= time:
                heapq.heappush(heap, (during, start))
        if len(heap) > 0:
            during, start = heapq.heappop(heap)
            last = time
            time += during
            answer += (time - start)
            cnt += 1
        else:
            time += 1

    answer //= N

    return answer




print(solution([[0, 3], [1, 9], [2, 6]]))

# answer
# 9