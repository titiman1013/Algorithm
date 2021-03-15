# def solution(s):
#     answer = True
    
#     que = []
#     for string in s:
#         if string == '(':
#             que.append(string)
#         elif string == ')':
#             if que:
#                 que.pop()
#             else:
#                 return False

#     if que: return False

#     return answer


# 그냥 숫자로 판별 가능

def solution(s):
    answer = 0

    for string in s:
        if answer < 0: return False
        
        if string == '(':
            answer += 1
        else:
            answer -= 1
    
    if answer == 0: return True
    else: return False





print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))

# answer
# true
# true
# false
# flase