import heapq

def solution(jobs):
    answer = 0

    time = 0
    heap = []
    for job in jobs:
        heapq.heappush(heap, (job[1], job[0]))
    
    while heap:
        during, intime = heapq.heappop(heap)
        if intime <= time:
            time += during
            answer += time - intime
        else:
            heapq.heappush(heap, (intime, during))

    return answer // len(jobs)




print(solution([[0, 3], [1, 9], [2, 6]]))

# answer
# 9