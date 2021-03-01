def solution(s, n):
    answer = ''

    s_list = list(map(str, s))
    for string in s_list:
        if string == ' ': 
            answer += ' '
            continue
        elif 64 < ord(string) <= 90:
            temp = ord(string) + n
            if temp > 90:
                temp = temp - 90 + 64
        elif 96 < ord(string) <= 122:
            temp = ord(string) + n
            if temp > 122:
                temp = temp - 122 + 96
        answer += chr(temp)

    return answer




print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))

# answer
# BC
# a
# e F d