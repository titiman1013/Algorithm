import sys; sys.stdin = open('simple binary password.txt', 'r')

example = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
    }

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    res = 0
    for i in range(N):
        password = []
        j = 0
        while j != M - 7:
            temp = ''
            for k in range(7):
                temp += arr[i][j+k]
            if temp in example:
                password.append(example[temp])
                # print(temp)
                j += 7
                # print(temp)
                if len(password) == 8:
                    break
            else:
                if password:
                    password.clear()
                    j -= 6
                else:
                    j += 1
        # print(len(password))
        if len(password) == 8:
            cnt = 0
            for p in range(8):
                if p % 2:
                    cnt += int(password[p])
                else:
                    cnt += int(password[p]) * 3
            if cnt % 10 == 0:
                for q in range(8):
                    res += int(password[q])
            break

    print(f'#{tc} {res}')