from itertools import permutations

def calc(expression_lst, order):
    for x_th in order:
        while x_th in expression_lst:
            oper_idx = expression_lst.index(x_th)
            a, b = expression_lst[oper_idx - 1], expression_lst[oper_idx + 1]
            if x_th == '*':
                tmp_calc = a * b
            elif x_th == '+':
                tmp_calc = a + b
            elif x_th == '-':
                tmp_calc = a - b
            expression_lst = expression_lst[:oper_idx - 1] + [tmp_calc] + expression_lst[oper_idx + 2:]
    return abs(expression_lst[0])


def solution(expression):
    answer = 0
    
    expression_lst = []
    operators = []
    tmp = ''
    for string in expression:
        if string == '+' or string == '-' or string == '*':
            if string not in operators:
                operators.append(string)
            expression_lst.append(int(tmp))
            tmp = ''
            expression_lst.append(string)
        if string.isnumeric():
            tmp += string
    expression_lst.append(int(tmp))

    oper_order = list(permutations(operators, len(operators)))
    for order in oper_order:
        result = calc(expression_lst, order)
        if result > answer:
            answer = result

    return answer



# 정규표현식 + eval function

import re
from itertools import permutations

def solution(expression):
    #1
    op = [x for x in ['*','+','-'] if x in expression]
    op = [list(y) for y in permutations(op)]
    ex = re.split(r'(\D)',expression)

    #2
    a = []
    for x in op:
        _ex = ex[:]
        for y in x:
            while y in _ex:
                tmp = _ex.index(y)
                _ex[tmp-1] = str(eval(_ex[tmp-1]+_ex[tmp]+_ex[tmp+1]))
                _ex = _ex[:tmp]+_ex[tmp+2:]
        a.append(_ex[-1])

    #3
    return max(abs(int(x)) for x in a)






print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))

# answer
# 60420
# 300