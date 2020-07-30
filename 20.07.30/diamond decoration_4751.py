import sys; sys.stdin = open('diamond decoration.txt', 'r')

for tc in range(1, int(input())+1):
    string = input()
    for i in range(5):
        res = '.'
        if i == 0 or i == 4:
            for j in range(len(string)):
                res += '.#..'
        elif i == 1 or i == 3:
            for j in range(len(string) * 2):
                res += '#.'
        elif i == 2:
            res = ''
            for j in range(len(string) + 1):
                if j == len(string):
                    res += '#'
                else:
                    res += '#.'
                    res += string[j]
                    res += '.'
        print(res)