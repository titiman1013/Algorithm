def solution(s):
    answer = 1001

    for num in range(1, len(s) // 2 + 1):
        string = ''
        for i in range(0, len(s), num):
            if i == 0:
                unit = s[:i + num]
                cnt = 1
            else:
                if unit == s[i:i + num]:
                    cnt += 1
                else:
                    if cnt > 1:
                        string += str(cnt) + unit
                    else:
                        string += unit
                    unit = s[i:i + num]
                    cnt = 1
                if i + num >= len(s):
                    if cnt > 1:
                        string += str(cnt)
                    string += unit
        if len(string) < answer:
            answer = len(string)

    if answer == 1001:
        answer = len(s)

    return answer




print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))