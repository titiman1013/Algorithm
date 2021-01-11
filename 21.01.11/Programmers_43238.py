def solution(n, times):
    answer = 0

    low, high = (n * min(times)) // len(times), n * max(times)
    while low <= high:
        mid = (low + high) // 2
        temp = 0
        for time in times:
            temp += mid // time
            if temp >= n:
                answer = mid
                high = mid - 1
                break
        if temp < n:
            low = mid + 1

    return answer



print(solution(6, [7, 10]))

# answer
# 28