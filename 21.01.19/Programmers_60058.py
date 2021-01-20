# false

# from collections import deque

# def solution(p):
#     answer = ''

#     w = p
#     u, v = check(w)
#     if len(u) != len(p):
#         u, v = revise(u, v)

#     return u



# def check(w):
#     stack = []
#     for i in range(len(w)):
#         if w[i] == '(':
#             stack.append('(')
#         else:
#             if len(stack) == 0:
#                 return w[:i], w[i:]
#             else:
#                 stack.pop()
#     return w, ''


# def revise(u, v):
#     deq = deque(v)
#     temp_open = []
#     temp_close = []
#     while deq:
#         val = deq.popleft()
#         if val == '(':
#             if len(temp_close):
#                 temp_open.append('(')
#                 if len(temp_open) == len(temp_close):
#                     for i in range(len(temp_open)):
#                         u += temp_open.pop()
#                     for i in range(len(temp_close)):
#                         u += temp_close.pop()
#             else:
#                 deq.appendleft(val)
#                 temp = ''
#                 for i in range(len(deq)):
#                     temp += deq[i]
#                 temp_u, temp_v = check(temp)
#                 u += ''.join(temp_u)
#                 deq = deque(temp_v)
#         else:
#             temp_close.append(')')
#     return u, deq


# false
# from collections import deque

# def solution(p):
#     answer = ''

#     u, v = division_open(p)
#     if len(u) != len(p):
#         u, v = revise(u, v)

#     return u
        

# def division_open(p):
#     stack = []
#     u = ''
#     for i in range(len(p)):
#         if p[i] == '(':
#             u += p[i]
#             stack.append(p[i])
#         else:
#             if len(stack):
#                 u += p[i]
#                 stack.pop()
#             else:
#                 return u, p[i:]
#     return u, ''


# def division_close(p):
#     stack = []
#     u = ''
#     for i in range(len(p)):
#         if p[i] == '(':
#             if len(stack):
#                 u += ')'
#                 stack.pop()
#             else:
#                 return u, p[i:]
#         else:
#             u += '('
#             stack.append(p[i])
#     return u, ''


# def revise(u, v):
#     deq = deque(v)
#     while deq:
#         val = deq.popleft()
#         if val == '(':
#             temp_u, temp_v = division_open(v)
#             u += temp_u
#             v = temp_v
#             deq = deque(v)
#         else:
#             temp_u, temp_v = division_close(v)
#             u += temp_u
#             v = temp_v
#             deq = deque(v)
#     return u, v



#

# def check(u):
#     temp = []
#     for i in u:
#         if i == '(':
#             temp.append(i)
#         else:
#             if len(temp):
#                 temp.pop()
#             else:
#                 return False
#     if len(temp):
#         return False
#     else:
#         return True


# def division(v):
#     temp = 0
#     for idx, val in enumerate(v):
#         if val == '(':
#             temp += 1
#         elif val == ')':
#             temp -= 1
#         if temp == 0:
#             return v[:idx + 1], v[idx + 1:]


# def solution(p):
#     # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
#     if p == '' or check(p): 
#         return p
    
#     # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
#     u, v = division(p)

#     # 3. 문자열 u가 "올바른 괄호 문자열" 이라면
#     if check(u):
#         # 문자열 v에 대해 1단계부터 다시 수행합니다.
#         answer = solution(v)
#         # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
#         return u + answer
#     # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
#     else:
#         # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
#         answer = '('
#         # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
#         answer += solution(v)
#         # 4-3. ')'를 다시 붙입니다.
#         answer += ')'
#         # 4-4. u의 첫 번째와 마지막 문자를 제거하고
#         u = list(u[1:-1])
#         # 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
#         for i in range(len(u)):
#             if u[i] == '(':
#                 u[i] = ')'
#             else:
#                 u[i] = '('
#         # 뒤에 붙입니다.
#         answer += "".join(u)
#         # 4-5. 생성된 문자열을 반환합니다.
#         return answer


# best solve

def solution(p):
    if p == '': return p
    check = True
    num = 0
    for i in range(len(p)):
        if p[i] == '(': num -= 1
        else: num += 1
        if num > 0: check = False
        if num == 0:
            if check:
                return p[:i + 1] + solution(p[i + 1:])
            else:
                return '(' + solution(p[i + 1:]) + ')' + "".join(list(map(lambda x: '(' if x == ')' else ')', p[1:i])))





print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
print(solution("))))()()()(())(((("))

# answer
# "(()())()"
# "()"
# "()(())()"