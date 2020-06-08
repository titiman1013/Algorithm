import sys; sys.stdin = open('number array rotate.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    nums = [list(map(int, input().split())) for i in range(N)]
     
    print(f'#{tc}')
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