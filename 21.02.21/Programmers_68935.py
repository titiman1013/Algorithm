def trans_reverse_ternary(num):
    res = ''
    while num > 0:
        quotient, remainder = divmod(num, 3)
        res += str(remainder)
        num = quotient
    return res


def trans_decimal(num):
    # int(변환할 숫자, 변환할 숫자의 진법) => 변환할 숫자를 10진법으로 바꿔줌
    return int(num, 3)


def solution(n):
    answer = 0

    answer = trans_decimal(trans_reverse_ternary(n))

    return answer




print(solution(45))
print(solution(125))