import sys; sys.stdin = open('text1.txt', 'r')

# time exceed

# def binary_search(temp_arr):
#     start, end = 0, max(temp_arr)
#     while start <= end:
#         temp = 0
#         mid = (start + end) // 2
#         for i in temp_arr:
#             if i >= mid:
#                 temp += i - mid
        
#         if temp >= M:
#             start += 1
#         else:
#             end -= 1
#     return end



# N, M = map(int, input().split())
# arr = list(map(int, input().split()))

# arr.sort()
# res = binary_search(arr)
# print(res)



# best solve
# 같은 높이의 나무들을 set화 시키기 때문에 반복 횟수가 줄어듬

from collections import Counter

def binary_search(temp_arr):
    start, end = 0, max(temp_arr)
    while start <= end:
        mid = (start + end) // 2
        temp = 0
        for val, cnt in temp_arr.items():
            if val > mid:
                temp += (val - mid) * cnt
        if temp >= M:
            res = mid
            start = mid + 1
        else:
            end = mid - 1
    return res



N, M = map(int, input().split())
arr = Counter(map(int, input().split()))

res = binary_search(arr)
print(res)