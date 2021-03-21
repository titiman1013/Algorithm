def solution(s):
    answer = []

    cnt = 0
    zero_cnt = 0
    while s != '1':
        cnt += 1
        zero_cnt += s.count('0')
        s = str(format(s.count('1'), 'b'))

    answer = [cnt, zero_cnt]

    return answer




print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))

# answer
# [3, 8]
# [3, 3]
# [4, 1]