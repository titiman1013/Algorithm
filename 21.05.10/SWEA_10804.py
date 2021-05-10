import sys; sys.stdin = open('10804.txt', 'r')

for tc in range(1, int(input()) + 1):
    strings = input()
    answer = []

    for string in strings:
        if string == 'b':
            answer.append('d')
        elif string == 'd':
            answer.append('b')
        elif string == 'p':
            answer.append('q')
        elif string == 'q':
            answer.append('p')
    
    answer = "".join(reversed(answer))

    print(f'#{tc} {answer}')