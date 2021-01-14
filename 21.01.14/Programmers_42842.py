def solution(brown, yellow):
    answer = []

    all = brown + yellow
    for i in range(min(3, min(brown, yellow)), max(brown, yellow)):
        if all / i == all // i:
            if (all // i + i - 2) * 2  == brown and all // i >= i:
                answer = [all // i, i]
                break

    return answer




print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))