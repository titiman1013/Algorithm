from itertools import permutations

def solution(expression):
    arr = []
    last = 0
    for i in range(len(expression)):
        if expression[i] == '+' or expression[i] == '-' or expression[i] == '*':
            arr.append(int(expression[last:i]))
            arr.append(expression[i])
            last = i + 1
    arr.append(int(expression[last:]))
    # print(arr)

    calc = []
    operator = ['+', '-', '*']
    order = list(permutations(operator, 3))
    # print(order)

    for i in range(len(order)):
        temp = arr.copy()
        # print(order[i])
        for j in range(len(order[i])):
            a = 0
            while True:
                if type(temp[a]) == str:
                    if temp[a] == order[i][j]:
                        mizi = temp.pop(a)
                        x = temp.pop(a-1)
                        a -= 1
                        y = temp.pop(a)
                        a += 1
                        if mizi == '*':
                            temp.insert(a-1, x * y)
                        elif mizi == '+':
                            temp.insert(a-1, x + y)
                        else:
                            temp.insert(a-1, x - y)
                        # print(';;')
                    else:
                        a += 1
                else:
                    a += 1
                # print(temp)
                if a == len(temp):
                    break
        calc.append(abs(temp[0]))

    answer = 0
    answer = max(calc)
    return answer


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))