def solution(a, b):
    answer = 0

    for val in range(min(a, b), max(a, b)+1):
        answer += val

    return answer




print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))

# answer
# 12
# 3
# 12