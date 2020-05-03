import sys; sys.stdin = open("password2.txt", "r")

for tc in range(1,11):
    n = int(input())
    code = list(input().split())
    cnt = int(input())
    rule = list(input().split())
    for i in range(len(rule)):
        if rule[i] == 'I':
            for j in range(int(rule[i+2])):
                code.insert(int(rule[i+1])+j,int(rule[i+3+j]))
        elif rule[i] == 'D':
            for j in range(int(rule[i+2])):
                code.pop(int(rule[i+1]))
    print('#{} '.format(tc),end="")
    print(*code[:10])