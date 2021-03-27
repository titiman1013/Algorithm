def solution(s):
    answer = ''

    s_lst = list(map(int, s.split()))
    s_lst.sort()
    answer += str(s_lst[0]) + ' ' + str(s_lst[-1])

    return answer




print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))

# answer
# "1 4"
# "-4 -1"
# "-1 -1"