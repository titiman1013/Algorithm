import sys; sys.stdin = open('bracket grouping.txt', 'r')

for tc in range(1, 11):
    length = int(input())
    arr = input()

    stack = []
    res = 0
    for i in range(length):
        if arr[i] == '(' or arr[i] == '[' or arr[i] == '{' or arr[i] == '<':
            stack.append(arr[i])
        elif arr[i] == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                break
        elif arr[i] == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                break
        elif arr[i] == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                break
        elif arr[i] == '>':
            if stack[-1] == '<':
                stack.pop()
            else:
                break

    if stack:
        pass
    else:
        res = 1

    print(f'#{tc} {res}')

# 코드 길이 줄여보기!