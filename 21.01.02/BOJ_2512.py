import sys; sys.stdin = open('text1.txt', 'r')

# false solve
# def check(temp_arr):
#     temp = 0
#     for i in range(N):
#         temp += temp_arr[i]
#     if temp <= M:
#         return temp

#     avg = temp // N
#     temp_arr.sort()
#     temp_lst = []
#     upper_lst = []
#     for i in range(N):
#         if temp_arr[i] <= avg:
#             temp_lst.append(temp_arr[i])
#         else:
#             upper_lst.append(temp_arr[i])
    
#     remain_val = M - sum(temp_lst)
#     remain_avg = remain_val // len(upper_lst)
#     for i in range(len(upper_lst)):
#         temp_lst.append(remain_avg)
#     print(temp_lst)
#     return max(temp_lst)



# N = int(input())
# arr = list(map(int, input().split()))
# M = int(input())

# res = check(arr)
# print(res)


# binary search

def binary_search(sort_arr):
    # start, end = sort_arr[0], sort_arr[-1]
    start, end = 0, sort_arr[-1]
    while start <= end:
        temp = 0
        mid = (start + end) // 2
        # print(start, mid, end)
        for i in range(N):
            if mid <= sort_arr[i]:
                temp += mid
            else:
                temp += sort_arr[i]
        if temp <= M:
            start = mid + 1
        else:
            end = mid - 1
        # print(start, mid, end)
        # print('------')
    return end
            


N = int(input())
arr = list(map(int, input().split()))
M = int(input())

arr.sort()
res = binary_search(arr)
print(res)