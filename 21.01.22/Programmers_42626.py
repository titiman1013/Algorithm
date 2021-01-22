import heapq

def solution(scoville, K):
    answer = 0

    # init
    heapq.heapify(scoville)

    min_val = scoville[0]
    while min_val < K:
        if len(scoville) < 2:
            answer = -1
            break
        val1 = heapq.heappop(scoville)
        val2 = heapq.heappop(scoville)
        val3 = val1 + val2 * 2
        heapq.heappush(scoville, val3)
        answer += 1
        min_val = scoville[0]

    return answer




print(solution([1, 2, 3, 9, 10, 12], 7))

# answer
# 2