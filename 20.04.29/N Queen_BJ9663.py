#
def dfs(row):
    global answer

    if row == N: answer += 1; return

    for c in range(N):
        if col[c] or right[c+row] or left[N+row-c-1]: continue
        col[c] = right[c+row] = left[N+row-c-1] = 1
        dfs(row+1)
        col[c] = right[c+row] = left[N+row-c-1] = 0

N = int(input())
col = [0]*N  # 열 체크
right = [0]*(2*N-1) # 오른 대각선 체크
left = [0]*(2*N-1)  # 왼 대각선 체크
answer = 0
dfs(0)
print(answer)


# # 
# N = int(input())
# isused1 = [0] * N
# isuesd2 = [0] * (N+N-1)
# isuesd3 = [0] * (N+N-1)

# def back_track(depth):
#     cnt = 0
#     if depth == N:
#             return 1
#     else:
#         for i in range(N):
#             if depth == 0 and i > (N-1)//2:
#                 break
#             if isused1[i] or isuesd2[depth+i] or isuesd3[depth-i+N-1]:
#                 continue
#             isused1[i] = isuesd2[depth + i] = isuesd3[depth - i + N - 1] = 1

#             if depth == 0 and i < (N-1)//2:
#                 cnt += back_track(depth+1) * 2
#             elif depth == 0 and i == (N-1)//2 and N % 2 == 0:
#                 cnt += back_track(depth+1) * 2
#             else:
#                 cnt += back_track(depth+1)

#             isused1[i] = isuesd2[depth + i] = isuesd3[depth - i + N - 1] = 0
#     return cnt
# print(back_track(0))


#
# #내 윗줄에 나와 겹치는 라인에 퀸이 있는가?
# def adjacent(x):
#     for i in range(x):
#         if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
#             return False
#     return True
        
        
# #한줄씩 재귀하며 DFS를 실행
# def dfs(x):
#     global result
    
#     if x == N:
#         result += 1

#     else:
#         for i in range(N):
#             row[x] = i
#             if adjacent(x):
#                 dfs(x + 1)

# N = int(input())
# row = [0] * N
# result = 0
# dfs(0)
# print(result)



# 입력 8
# 출력 92