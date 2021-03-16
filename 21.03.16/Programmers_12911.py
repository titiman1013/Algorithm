def solution(n):
    answer = 0

    num = n + 1
    while True:
        if str(format(num, 'b')).count('1') == str(format(n, 'b')).count('1'):
            return num
        num += 1

    return answer




print(solution(78))
print(solution(15))

# answer
# 83
# 23