import sys; sys.stdin = open('Olymphic.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    ranks = list(map(int, input().split()))
    min_prices = list(map(int, input().split()))
    vote_list = [0] * N

    for i in range(len(min_prices)):
        temp = N + 1
        for idx, rank in enumerate(ranks):
            if min_prices[i] >= rank:
                if idx < temp:
                    temp = idx
        vote_list[temp] += 1
    
    result = 0
    cnt = 0
    for i in range(N):
        if vote_list[i] > cnt:
            cnt = vote_list[i]
            result = i
    
    print(f'#{tc} {result+1}')