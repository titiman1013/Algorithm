def solution(s):
    answer = ''

    idx = 0
    for string in s:
        if string == ' ':
            idx = 0
            answer += ' '
            continue
        elif idx % 2:
            answer += string.lower()
        else:
            answer += string.upper()
        idx += 1

    return answer




print(solution("try hello world"))

# answer
# "TrY HeLlO WoRlD"