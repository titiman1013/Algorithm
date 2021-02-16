# def solution(s):
#     answer = ''

#     length = len(s)
#     if length % 2:
#         answer = s[length // 2]
#     else:
#         answer = s[length // 2 - 1:length // 2 + 1]

#     return answer


# short coding

def solution(s):
    return str[(len(s) - 1) // 2:len(s) // 2 + 1]





print(solution("abcde"))
print(solution("qwer"))

# answer
# c
# we