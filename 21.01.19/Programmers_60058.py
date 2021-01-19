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
        




print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))