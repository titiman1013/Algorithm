import sys; sys.stdin = open('string.txt', 'r')

# 답
# 2

#
# for tc in range(1, int(input())+1):
#     arr = list(input().split())

#     temp = 0
#     for i in range(len(arr[0])):
#         ttemp = 0
#         for j in range(len(arr[1])):
#             if arr[0][i] == arr[1][j]:
#                 k = 0
#                 while arr[0][i+k] == arr[1][j+k]:
#                     if i+k < len(arr[0]) and j+k < len(arr[1]):
#                         k += 1
#                     else:
#                         break
#                 ttemp += k
#         if temp < ttemp:
#             temp = ttemp
    
#     res = len(arr[0]) - temp
#     print(res)

#
for tc in range(1, int(input())+1):
    arr = list(input().split())

    res = 0
    for i in range(len(arr[1])-len(arr[0])+1):
        temp = 0
        k = 0
        while k != len(arr[0]):
            if arr[0][k] == arr[1][i+k]:
                # print(arr[0][k])
                temp += 1
            k += 1
        if temp > res:
            res = temp
    
    print(len(arr[0]) - res)