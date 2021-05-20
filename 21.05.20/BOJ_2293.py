import sys; sys.stdin = open('2293.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    coins = list(int(input()) for _ in range(N))

    dp = [0 for _ in range(K + 1)]
    dp[0] = 1

    for coin in coins:
        for i in range(coin, K + 1):
            if i - coin >= 0:
                dp[i] += dp[i - coin]
    
    print(dp[K])