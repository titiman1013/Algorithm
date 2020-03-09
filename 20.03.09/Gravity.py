import sys
sys.stdin = open("Gravity.txt" , "r")

# for t in range(int(input())):
#     boxs = list(map(int, input().split()))
#     arr = [[0] * 9] * 8

#     for box in range(len(boxs)):
#         for j in range(7, -1, -1):
#             arr[j][box] = 1
    
# 떨어뜨리는 개념이 아니라 제일 높은 위치에 있는 상자의 낙차값만 구하면 된다


# 
for t in range(int(input())):
    # 모든 꼭대기의 상자에 대해서 반복 수행
    arr = list(map(int, input().split()))
    N = len(arr)
    ans = 0
    for i in range(N):    
        # arr[0] -> arr[N - 1] 까지 (밑에 오는 상자들이 없다면) 낙차값
        h = N - 1 - i    # 상자위치에서 바닥까지 거리
        if ans >= h:
            break
        # 자기 밑에 오는 상자의 수를 카운팅
        for j in (i + 1, N):
            if arr[i] <= arr[j]:   # 밑에 오는 상자
                h -= 1
        ans = max(ans, h)