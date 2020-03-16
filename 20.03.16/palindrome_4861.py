import sys; sys.stdin = open('palindrome.txt', 'r')

# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     # N은 행열의 수 M은 찾아야하는 회문의 글자수
#     arr = [list(map(list, input().split())) for _ in range(N)]

#     res = []
#     for i in range(N-M+1):
#         if len(res) != 0:
#             break
#         for j in range(N-M+1):
#             if arr[i][j] == arr[i][j+M]:
#                 cnt = 0
#                 for k in range(M//2):
#                     if (j + M) < N:
#                         if arr[i][j+k] == arr[i][j+M-k]:
#                             cnt += 1
#                         else: break
#                 if cnt == M//2:
#                     res = arr[i][j:j+M]
#                     break
#             elif arr[j][i] == arr[j][i+M]:
#                 cnt = 0
#                 for k in range(M//2):
#                     if (j + M) < N:
#                         if arr[j][i+k] == arr[j][i+M-k-1]:
#                             cnt += 1
#                         else: break
#                 if cnt == M//2:
#                     for k in range(M):
#                         res.append(arr[j][i+k])
#                     break
    
#     print(f'#{tc}', end=' ')
#     for _ in range(len(res)):
#         print(res[_], end='')
#     print()

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    # 가로탐색
    for i in range(N):
        for j in range(N-M+1):
            if arr[i][j] == arr[i][j+M-1]


#