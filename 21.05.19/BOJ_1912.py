import sys; sys.stdin = open('1912.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    
    dp = [val for val in nums]
    for i in range(1, N):
        dp[i] = max(dp[i], dp[i - 1] + nums[i])
    
    print(max(dp))