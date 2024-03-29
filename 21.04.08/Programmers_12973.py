# false

# def solution(s):
#     answer = 0

#     idx = 0
#     while len(s):
#         if len(s) == 1: break

#         if s[idx] == s[idx + 1]:
#             while s[idx] == s[idx + 1]:
#                 if idx + 1 == len(s) - 1: 
#                     return 1
#                 idx += 1
#             s = s[:idx - 1] + s[idx + 1:]
#             idx = 0
#             continue
        
#         if idx + 1 == len(s) - 1:
#             break
        
#         idx += 1

#     return answer


#

def solution(s):
    answer = 0

    stack = []
    for string in s:
        if stack:
            if stack[-1] == string:
                stack.pop()
            else:
                stack.append(string)
        else:
            stack.append(string)

    if stack:
        answer = 0
    else:
        answer = 1

    return answer




print(solution("baabaa"))
print(solution("cdcd"))

# answer
# 1
# 0