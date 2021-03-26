import sys; sys.stdin = open('1224.txt', 'r')

#

# def calc(operate, a, b):
#     if operate == '+':
#         return str(int(a) + int(b))
#     elif operate == '*':
#         return str(int(a) * int(b))



# for tc in range(1, 11):
#     N = int(input())
#     strings = input()

#     answer = 0
#     nums = []
#     operator = []
#     paren = 0  # parentheses
#     go = False

#     for string in strings:
#         if string.isnumeric():
#             nums.append(string)
#             if go:
#                 go = False
#                 nums.append(calc(operator.pop(), nums.pop(), nums.pop()))
#         elif string == '(':
#             paren += 1
#         elif string == ')':
#             if paren == 1:
#                 paren -= 1
#                 nums.append(calc(operator.pop(), nums.pop(), nums.pop()))
#             else:
#                 answer = False
#                 break
#         else:
#             if string == '*':
#                 go = True
#             operator.append(string)
    
#     while operator and nums:
#         nums.append(calc(operator.pop(), nums.pop(), nums.pop()))
    
#     if len(nums) == 1:
#         answer = int(nums[0])
#     else:
#         answer = False

#     print(f'#{tc} {answer}')



#

# in-stack
isp = {
    '*': 2,
    '+': 1,
    '(': 0,
}
# in-coming
icp = {
    '*': 2,
    '+': 1,
    '(': 3,
}

for tc in range(1, 11):
    N = int(input())
    strings = input()

    # 완성된 식
    coms = []
    opers = []
    for string in strings:
        if string.isnumeric():
            coms.append(string)
        else:
            if string == ')':
                for oper in opers[::-1]:
                    if oper == '(':
                        opers.pop()
                        break
                    else:
                        coms.append(opers.pop())
            else:
                if opers:
                    for oper in opers[::-1]:
                        if isp[oper] < icp[string]:
                            opers.append(string)
                            break
                        else:
                            coms.append(opers.pop())
                else:
                    opers.append(string)
    for oper in opers[::-1]:
        coms.append(oper)
    stack = []
    for com in coms:
        if com.isnumeric():
            stack.append(int(com))
        else:
            a, b = stack.pop(), stack.pop()
            if com == "+":
                stack.append(a + b)
            elif com == "*":
                stack.append(a * b)
    
    answer = stack[0]
    print(f'#{tc} {answer}')