# def trans_notation(n, number):
#     tmp = ''
#     while number // n:
#         quotient, remainder = number // n, number % n
#         tmp += str(remainder)
#         number = quotient
#     tmp += str(number)
#     return tmp[::-1]

import string

ascii = string.digits + string.ascii_uppercase

def trans_notation(n, number):
    q, r = divmod(number, n)
    if q == 0:
        return ascii[r]
    else:
        return trans_notation(n, q) + ascii[r]


def solution(n, t, m, p):
    answer = ''

    result_list = ''
    number = 0
    while len(result_list) <= t * m:
        trans_num = trans_notation(n, number)
        result_list += trans_num
        number += 1
    
    for i in range(p - 1, len(result_list), m):
        answer += result_list[i]
        if len(answer) == t:
            break

    return answer




print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))

# answer
# "0111"
# "02468ACE11111111"
# "13579BDF01234567"