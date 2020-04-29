import sys; sys.stdin = open('binary.txt', 'r')

for tc in range(1, int(input())+1):
    print(f'#{tc}', end=' ')
    cnt, num = input().split()
    for i in num:
        if i.isdigit():
            res = bin(int(i))
        else:
            ten = int('0x'+i, 16)
            res = bin(ten)
        res = str(res)[2:]
        if len(res) != 4:
            temp = 4 - len(res)
            res = '0' * temp + res
        print(res, end='')
    print()