import sys; sys.stdin = open('1230.txt', 'r')

def insert(x, y, s):
    password_f, password_b = passwords[:x] + s, passwords[x:]
    return password_f + password_b


def delete(x, y):
    password_f, password_b = passwords[:x], passwords[x + y:]
    return password_f + password_b


def add(y, s):
    return passwords + s



for tc in range(1, 11):
    N = int(input())
    passwords = list(map(int, input().split()))
    M = int(input())
    orders = list(map(str, input().split()))

    idx = 0
    while idx < len(orders):
        if orders[idx].isalpha():
            if orders[idx] == 'I':
                passwords = insert(int(orders[idx + 1]), int(orders[idx + 2]), list(map(int, orders[idx + 3:idx + 3 + int(orders[idx + 2])])))
                idx += int(orders[idx + 2]) + 3
            elif orders[idx] == 'D':
                passwords = delete(int(orders[idx + 1]), int(orders[idx + 2]))
                idx += 3
            else:
                passwords = add(int(orders[idx + 1]), list(map(int, orders[idx + 2:idx + 2 + int(orders[idx + 1])])))
                idx += int(orders[idx + 1]) + 2
        else:
            break
    
    print(f'#{tc}', end = ' ')
    for i in range(10):
        print(passwords[i], end=' ')
    print()