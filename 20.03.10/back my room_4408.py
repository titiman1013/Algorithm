# import sys; sys.stdin = open('back my room.txt', 'r')

# for tc in range(1, int(input())+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for i in range(N)]
    
#     result = 0
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if i != j:
#                 if arr[j][0] <= arr[i][0] <= arr[j][1] or arr[j][0] <= arr[i][1] <= arr[j][1]:
                    
#                     result += 1
    
#     print(f'#{tc} {result}')


#
import sys; sys.stdin = open('back my room.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())

    cnt = [0] * 201
    for _ in range(N):
        a, b = map(int, input().split())    # a --> b

        a = (a + 1) // 2
        b = (a + 1) // 2

        if a > b: a, b = a, b

        for i in range(a, b + 1):
            cnt[i] += 1     # 복도에 표시

    # 겹치는 동선을 찾아서 가장 최댓값을 출력하면 됨