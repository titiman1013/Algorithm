import sys; sys.stdin = open('5162.txt', 'r')

for tc in range(1, int(input()) + 1):
    cost_A, cost_B, total = map(int, input().split())

    answer = max(total // min(cost_A, cost_B), (total // (cost_A + cost_B) * 2))
    
    print(f'#{tc} {answer}')