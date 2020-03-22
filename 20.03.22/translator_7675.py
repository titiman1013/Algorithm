import sys; sys.stdin = open('translator.txt', 'r')

# for tc in range(1, int(input())+1):
#     N = int(input())
#     arr = input()
    
#     arr_list = []
#     temp = 0
#     print(arr)
#     for i in range(len(arr)):
#         if arr[i] == '!' or arr[i] == '?' or arr[i] == '.':
#             if arr[temp] == ' ':
#                 temp = i + 1
#                 continue
#             arr_list.append(arr[temp:i])
#             temp = i + 1
#     print(arr_list)

# #     res = [0] * N
# #     for i in range(len(arr_list)):
# #         if arr_list[i][0].isupper():
# #             temp = 1
# #             for j in range(1, len(arr_list[i])):
# #                 if arr_list[i][j].islower():
# #                     temp += 1
# #             if temp == len(arr_list[i]):
# #                 res[i] += 1



# #     print(f'#{tc}', end=' ')
# #     for i in range(N):
# #         print(i, end=' ')
# #     print()

for tc in range(1, int(input())+1):
    N = int(input())
    arr = input()

    cut = 0
    arr_list = []
    for i in range(len(arr)):
        if arr[i] == '!' or arr[i] == '?' or arr[i] == '.':
            arr_list.append(arr[cut:i])
            cut = i + 1
    
    for i in range(N):
        arr_list[i] = list(arr_list[i].split())

    res = [0] * N
    for i in range(N):
        for j in range(len(arr_list[i])):
            if arr_list[i][j][0].isupper():
                temp = 1
                for k in range(len(arr_list[i][j])):
                    if arr_list[i][j][k].islower():
                        temp += 1
                if temp == len(arr_list[i][j]):
                    res[i] += 1
    
    print(f'#{tc}', end=' ')
    for i in range(N):
        print(res[i], end=' ')
    print()