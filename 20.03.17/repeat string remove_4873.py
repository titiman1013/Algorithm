import sys; sys.stdin = open("repeat string remove.txt", "r")

#
T = int(input())
for tc in range(1, T+1):
    s = input()
    top = -1    # 가장 마지막으로 저장된 원소의 인덱스
    stack = [0] * 1000
    top += 1    # push(s[0])
    stack[top] = s[0]   # push(s[0])
    for i in range(1, len(s)):
        if stack[top] == s[i]:
            top -= 1
        else:
            top += 1
            stack[top] = s[i]
    print('#{} {}'.format(tc, top+1))