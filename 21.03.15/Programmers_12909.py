def solution(s):
    answer = True
    
    que = []
    for string in s:
        if string == '(':
            que.append(string)
        elif string == ')':
            if que:
                que.pop()
            else:
                return False

    if que: return False

    return answer




print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))

# answer
# true
# true
# false
# flase