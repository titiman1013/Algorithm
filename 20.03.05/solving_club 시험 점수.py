import sys
sys.stdin = open("시험점수.txt", "r")

# 시간초과
# def _sum(cnt):
#     if cnt == N:
#         temp = 0
#         for i in range(N):
#             if check[i] == True:
#                 temp += score[i]
#         result.add(temp)
#         return
    
#     check[cnt] = True
#     _sum(cnt+1)
#     check[cnt] = False
#     _sum(cnt+1)





# T = int(input())
# for t in range(T):
#     N = int(input())
#     score = list(map(int, input().split()))
#     result = set()
#     check = [False] * N
#     _sum(0)
#     print(f'#{t+1} {len(result)}')



# T = int(input())
# for t in range(T):
#     N = int(input())
#     scores = list(map(int, input().split()))
#     result = [0]

#     for score in scores:
#         for i in range(len(result)):
#             result = list(result)
#             result.append(result[i] + score)
#         result = set(result)

#     print(f'#{t+1} {len(result)}')



T = int(input())
for t in range(T):
    N = int(input())
    scores = list(map(int, input().split()))
    result = {0}

    for score in scores:
        result_list = list(result)
        for i in range(len(result_list)):
            result.add(result_list[i] + score)

    print(f'#{t+1} {len(result)}')




# T = int(input())
# for t in range(T):
#     N = int(input())
#     scores = list(map(int, input().split()))
#     result = [0]

#     for score in scores:
#         for i in range(len(result)):
#             if result[i] + score not in result:
#                 result.append(result[i] + score)

#     print(f'#{t+1} {len(result)}')


# for t in range(1,1+int(input())):
#     input();s=map(int,input().split());a=1
#     for i in s:a|=a<<i
#     print('#%i'%t,bin(a).count('1'))
