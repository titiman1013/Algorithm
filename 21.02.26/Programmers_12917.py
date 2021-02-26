def solution(s):
    answer = ''

    # return "".join(sorted(list(map(str, s)), reverse=True))

    # 문자열도 정렬됨
    return "".join(sorted(s, reverse=True))




print(solution("Zbcdefg"))

# answer
# "gfedcbZ"