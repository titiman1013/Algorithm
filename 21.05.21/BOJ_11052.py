import sys; sys.stdin = open('11052.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    cards = [0] + list(map(int, input().split()))

    dp = [0 for _ in range(N + 1)]
    for cnt in range(1, N + 1):
        for k in range(1, cnt + 1):
            dp[cnt] = max(dp[cnt], dp[cnt - k] + cards[k])
    
    print(max(dp))



# answer
# 10
# 50
# 55
# 50
# 20
# 18