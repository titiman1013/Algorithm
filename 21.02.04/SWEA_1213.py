import sys; sys.stdin = open('1213.txt', 'rt', encoding='UTF-8')

for _ in range(1, 11):
    tc = int(input())
    target = input()
    strings = input()

    answer = 0
    idx = 0
    while idx <= len(strings) - len(target):
        if strings[idx:idx+len(target)] == target:
            answer += 1
            idx += len(target)
        else:
            idx += 1
    print(f'#{tc} {answer}')