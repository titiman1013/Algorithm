def solution(arr, divisor):
    answer = []

    for val in arr:
        if val % divisor == 0:
            answer.append(val)
    
    if len(answer):
        answer.sort()
    else:
        answer.append(-1)

    return answer




print(solution([5, 9, 7, 10], 5))
print(solution([2, 36, 1, 3], 1))
print(solution([3, 2, 6], 10))