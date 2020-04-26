# 1
# N = int(input())
# arr = [int(input()) for _ in range(N)]

# num_list = [[] for _ in range(N)]
# for i in range(N):
#     for j in range(2, arr[i]):
#         if i == 0:
#             num_list[arr[i]%j].append(j)
#             # print(num_list)
#         else:
#             if arr[i] % j in num_list[i-1] and arr[i] % j not in num_list[i]:
#                 num_list[arr[i]%j].append(j)
#                 # print(num_list)
#                 if j not in res_list:
#                     res_list.append(j)
#         if num_list[i]:
#             list(set(num_list[i]))

# print(res_list[-1])

# 2
# N = int(input())
# arr = [int(input()) for _ in range(N)]

# num_list = [[] for _ in range(arr[-1])]
# for i in range(N):
#     for j in range(2, arr[i]):
#         if j not in num_list[arr[i]%j]:
#             num_list[arr[i]%j].append(j)
# print(num_list)
# res_list = []
# for i in range(len(num_list)):
#     if len(num_list) == N:
#         res_list.append(i)

# for i in res_list:
#     print(i)

# # 3
# N = int(input())
# arr = [int(input()) for _ in range(N)]

# res_list = [[] for _ in range(arr[0]+1)]
# for i in arr:
#     for j in range(2, arr[0]+1):
#         res_list[j].append(i%j)
# # print(res_list)

# res = []
# for i in range(len(res_list)):
#     if len(res_list[i]) == N:
#         temp = res_list[i][0]
#         for j in range(1, N):
#             if temp != res_list[i][j]:
#                 break
#         else:
#             res.append(i)

# for i in res:
#     print(i, end=' ')

#
import sys 
import math 

N = int(input()) 
nums = [] 
for i in range(N): 
    nums.append(int(input())) 
# nums.sort() 

mog = nums[-1] - nums[0] 
divisor = [mog] 
for i in range(2, int(math.sqrt(mog)) + 1): 
    if mog % i == 0: 
        divisor.append(i) 
        divisor.append(mog//i) 
divisor = list(set(divisor)) 
# divisor.sort() 

for d in divisor: 
    for i in range(N): 
        if i == N - 1: 
            print(d, end = " ") 
        elif nums[i] % d != nums[i + 1] % d: 
            break