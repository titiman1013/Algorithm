def solution(n):
    if n <= 3:
        return '124'[n - 1]
    else:
        div, mod = divmod(n - 1, 3)
        return solution(div) + '124'[mod]




print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))
print(solution(8))
print(solution(9))

# answer
# 1
# 2
# 4
# 11