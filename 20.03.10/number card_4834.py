import sys; sys.stdin = open('number card.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    cards = list(map(int, list(input())))
    count = [0] * 10

    for card in cards:
        count[card] += 1

    number = 0
    cnt = 0
    for i in range(len(count)):
        if cnt <= count[i]:
            cnt = count[i]
            number = i

    print(f'#{tc} {number} {cnt}')