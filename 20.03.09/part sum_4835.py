# import sys; sys.stdin = open('part sum.txt', 'r')

# for t in range(int(input())):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))

#     Max = 0
#     Min = 1000000
#     for i in range(N-M+1):
#         temp = 0
#         for j in range(M):
#             temp += arr[i+j]
#         if Max < temp:
#             Max = temp
#         if Min > temp:
#             Min = temp
        
#     print(f'#{t+1} {Max-Min}')


#
import sys; sys.stdin = open('part sum.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 모든 가능한 구간합을 구한다.
    # 구간의 시작위치 0 ~ N - M
    Min = 10000000
    Max = 0
    for i in range(N - M + 1):
        # 시작위치 부터 M개의 자료를 읽는다 -> 합
        S = 0
        # S = sum(arr[i: i + M])으로 for문을 하나 줄일 수도 있다
        for j in range(M): # j = 0 ~ M - 1
            S += arr[i + j]
        # 최대, 최소로 저장
        Min = min(Min, S)
        Max = max(Max, S)
    
    print('#{} {}'.format(tc, Max-Min))