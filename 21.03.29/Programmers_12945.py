def solution(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a




print(solution(3))
print(solution(5))

# answer
# 2
# 5