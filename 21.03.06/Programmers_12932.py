def solution(n):
    # answer = []

    # answer = list(map(int, str(n)))

    # return answer[::-1]

    return list(map(int, reversed(str(n))))




print(solution(12345))

# answer
# [5, 4, 3, 2, 1]