import sys; sys.stdin = open('card.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    cards = [int(input()) for _ in range(N)]
    
    res_dict = {}
    for card in cards:
        if card in res_dict:
            res_dict[card] += 1
        else:
            res_dict[card] = 1
    
    value = 0
    res = 0
    for key, val in res_dict.items():
        if val > value:
            res = key
            value = val
        elif val == value:
            if key < res:
                res = key
                value = val
    
    print(res)



# 답
#1 1
#2 1