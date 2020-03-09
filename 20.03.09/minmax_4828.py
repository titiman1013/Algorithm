# import sys
# sys.stdin = open('minmax.txt', 'r')

# T = int(input())
# for t in range(T):
#     N = int(input())
#     nums = list(map(int, input().split()))
#     print(f'#{t+1} {max(nums)-min(nums)}')


#
import sys; sys.stdin = open('minmax.txt', 'r')

for tc in range(1, int(input()) + 1):   # tc 값을 출력하기 위해 1부터 T까지
    N = int(input())
    arr = list(map(int, input().split()))

    Max = 0
    Min = 100000000
    for i in range(N):
        if arr[i] < Min: Min = arr[i]
        if arr[i] > Max: Max = arr[i]
    
    print('#{} {}'.format(tc, Max-Min))