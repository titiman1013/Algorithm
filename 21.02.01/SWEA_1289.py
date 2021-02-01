import sys; sys.stdin = open('1289.txt', 'r')

for tc in range(1, int(input()) + 1):
    ori = input()

    res = '0' * len(ori)
    answer = 0
    for i in range(len(ori)):
        if res[i] != ori[i]:
            temp = res[:i]
            res = temp + ori[i] * (len(ori) - len(temp))
            answer += 1
        
        if res == ori: break
    print(f'#{tc} {answer}')