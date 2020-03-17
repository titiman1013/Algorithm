import sys; sys.stdin = open("bracket inspection.txt", "r")

for tc in range(1, int(input())+1):
    strings = input()

    stack = []
    for string in strings:
        if string == '(' or string == '{':
            stack.append(string)
        elif string == ')' or string == '}':
            if stack:
                if stack[-1] == '(' and string == ')':
                    stack.pop()
                elif stack[-1] == '{' and string == '}':
                    stack.pop()
                else:
                    break
            else:
                stack.append(1)
                break
    if stack == False:
        if ('(' and ')' and '{' and '}') not in strings:
            stack.append(1)
    print(f'#{tc}', end=' ')
    if stack:
        print(0)
    else:
        print(1)

# #
# def f(s):
#     stack = []
#     for i in range(len(s)):
#         if s[i] == '{' or s[i] == '(':      # 괄호 시작 push
#             stack.append(s[i])
#         elif s[i] == '}' or s[i] == ')':    # 괄호 닫음 pop 
#             if not stack:   # 스택(리스트)가 비어있으면 0
#                 return 0
#             r = stack.pop()
#             if (s[i] == '}' and r == '(') or (s[i] == ')' and r == '{'):
#                 return 0    # 짝이 아닌 경우 0 반환
#     if len(stack) == 0:     # 문자열에 괄호도 없고 스택도 비어 있으면
#         return 1    # 모든 괄호가 짝이 맞은 경우 1
#     else:
#         return 0    # 스택에 남은게 있으면 0

# T = int(input())
# for tc in range(1, T+1):
#     s = input()
#     print('#{} {}'.format(tc, f(s)))