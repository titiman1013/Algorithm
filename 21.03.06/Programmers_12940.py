# 유클리드 호제법

# 계속 b를 a로, 'a를 b로 나눈 나머지'를 b로 대입시켜 b가 0이 될때 까지 반복하면 남는 a가 최대 공약수
def GCD(num1, num2):
    x, y = min(num1, num2), max(num1, num2)
    while y:
        x, y = y, x % y
    return x


# 최소 공배수는 a, b의 곱을 최대 공약수로 나눈 것
def LCM(num1, num2):
    x, y = min(num1, num2), max(num1, num2)
    res = (x * y) // GCD(x, y)
    return res


def solution(n, m):
    answer = []

    answer = [GCD(n, m), LCM(n, m)]

    return answer




print(solution(3, 12))
print(solution(2, 5))

# answer
# [3, 12]
# [1, 10]