import sys; sys.stdin = open('danzo.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    nums = list(map(int, input().split()))

    # N개의 값들에서 2개 선택해서 곱하는 모든 경우
    ans = -1
    for i in range(N-1):
        for j in range(i+1, N):
            num = nums[i] * nums[j]
            
            if ans >= num: continue     # 실행시간을 줄일 방법(없어도 무방)

            t = num
            b = t % 10
            t //= 10
            while t:
                a = t % 10
                if a > b: break
                t //= 10
                b = a
            else:   # 단조증가하는 수
                ans = max(ans, num)

    print(f'#{tc} {ans}')



    # 출력시 단조 증가하는 경우가 없으면 -1을 출력