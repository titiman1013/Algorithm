import sys; sys.stdin = open('10570.txt', 'r')

for tc in range(1, int(input()) + 1):
    answer = 0

    A, B = map(int, (input().split()))
    for i in range(A, B + 1):
        if int(i ** (1 / 2)) ** 2 == i:
            # 원래 값과 제곱근이 1글자 일 때
            if len(str(i)) == 1:
                if len(str(int(i ** (1 / 2)))) == 1:
                    answer += 1
            
            elif str(i)[:len(str(i)) // 2] == str(i)[len(str(i)) // 2 + 1:]:
                if len(str(int(i ** (1 / 2)))) % 2:
                    if str(int(i ** (1 / 2)))[:len(str(int(i ** (1 / 2)))) // 2] == str(int(i ** (1 / 2)))[len(str(int(i ** (1 / 2)))) // 2 + 1:]:
                        answer += 1
                else:
                    if str(int(i ** (1 / 2)))[:len(str(int(i ** (1 / 2)))) // 2] == str(int(i ** (1 / 2)))[len(str(int(i ** (1 / 2)))) // 2:]:
                        answer += 1
    
    print(f'#{tc} {answer}')