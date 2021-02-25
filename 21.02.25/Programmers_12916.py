def solution(s):
    # answer = True

    # cnt = 0
    # for string in s.lower():
    #     if string == 'p': cnt += 1
    #     elif string == 'y': cnt -= 1
    
    # if not cnt == 0:
    #     answer = False

    # return answer

    return s.lower().count('p') == s.lower().count('y')




print(solution("pPoooyY"))
print(solution("Pyy"))

# answer
# true
# false