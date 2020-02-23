import sys
sys.stdin = open("숫자배열회전.txt", "r")

T = int(input())
for t in range(T):
    N = int(input())
    nums = [list(map(int, input().split())) for i in range(N)]
    print(f'#{t+1}')
    for k in range(N):
        for i in range(N):
            for j in range(N):
                print(nums[-j-1][k], end='')
            break
        print('', end = ' ')
        for i in range(N):
            for j in range(N):
                print(nums[-1-k][-j-1], end='')
            break
        print('', end = ' ')
        for i in range(N):
            for j in range(N):
                print(nums[j][-k-1], end='')
            break
        print('')