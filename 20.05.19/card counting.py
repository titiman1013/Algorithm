import sys; sys.stdin = open('card counting.txt', 'r')

T = int(input())
for n in range(T):
    cards = input()
    
    temps = []
    for i in range(0, len(cards), 3):
        temps.append(cards[i:i+3])
    
    temps_dict = {}
    for temp in temps:
        if temp not in temps_dict:
            temps_dict[temp] = 1
        else:
            temps_dict[temp] += 1
     
    print(f'#{n+1}', end=' ')
    
    result = {'S': 0, 'D': 0, 'H': 0, 'C': 0}
    for key in temps_dict:
        if key[0] in result:
            result[key[0]] += 1
    
    final = []
    for i in result.values():
        final.append(13-i)
    for i in temps_dict.values():
        if i >= 2:
            final.clear()
            final.append('ERROR')
    for i in final:
        print(f'{i}', end=' ')
    print('')