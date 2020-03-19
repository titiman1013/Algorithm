import sys; sys.stdin = open('Forth.txt', 'r')

# for tc in range(1, int(input())+1):
#     arr = list(input().split())
    
#     stack = []
#     for i in arr:
#         if i.isdecimal():
#             stack.append(int(i))
#         else:
#             if i == '.':
#                 if len(stack) != 1:
#                     stack.clear()
#                     stack.append('error')
#                 break
#             elif len(stack) < 2:
#                 stack.clear()
#                 stack.append('error')
#                 break
#             else:
#                 b = stack.pop()
#                 a = stack.pop()                
#                 if i == '+':
#                     stack.append(a+b)
#                 elif i == '-':
#                     stack.append(a-b)
#                 elif i == '*':
#                     stack.append(a*b)
#                 elif i == '//':
#                     stack.append(a/b)
    
#     print(f'#{tc} {stack[0]}')


#
def f():
    s = []
    for i in range(len(code)):
        if code[i] == '+' or code[i] == '-' or code[i] == '/' or code[i] == '*':
            if len(s) >= 2:
                op2 = int(s.pop())
                op1 = int(s.pop())
                if code[i] == '+':
                    s.append(op1+op2)
                elif code[i] == '-':
                    s.append(op1-op2)
                elif code[i] == '*':
                    s.append(op1*op2)
                elif code[i] == '/':
                    s.append(op1//op2)
            else:
                return 'error'        
        elif code[i] != '' and code[i] != '.':
            s.append(code[i])
        elif code[i] == '.':
            if len(s) == 1:
                return s.pop()
            else:
                return 'error'


T = int(input())
for tc in range(1, T+1):
    code = list(input().split())

    print('# {} {}'.format(tc, f()))