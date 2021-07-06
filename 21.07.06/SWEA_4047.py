import sys; sys.stdin = open('4047.txt', 'r')


patterns = {
    'S': 0,
    'D': 1,
    'H': 2,
    'C': 3,
}

for tc in range(1, int(input()) + 1):
    cards_info = input()

    answer = [13, 13, 13, 13]
    card_list = dict()
    for i in range(0, len(cards_info), 3):
        card_info = cards_info[i:i + 3]
        if card_list.get(card_info):
            answer = 'ERROR'
            break
        else:
            card_list[card_info] = 1
            answer[patterns.get(card_info[0])] -= 1
    
    print(f'#{tc}', end=" ")
    print(*answer) if type(answer) == list else print(answer)