def move(s, x):
    return s[x:] + s[:x]


def check(s):
    stack = []
    for string in s:
        if string == '(' or string == '[' or string == '{':
            stack.append(string)
        else:
            if stack:
                if string == ')':
                    if stack[-1] == '(': stack.pop()
                    else: return False
                elif string == ']':
                    if stack[-1] == '[': stack.pop()
                    else: return False
                elif string == '}':
                    if stack[-1] == '{': stack.pop()
                    else: return False
            else: return False
    return False if stack else True


def solution(s):
    answer = -1

    answer = 0
    for x in range(len(s)):
        s_tmp = move(s, x)
        if check(s_tmp):
            answer += 1

    return answer




print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))
print(solution('((('))

# answer
# 3
# 2
# 0
# 0