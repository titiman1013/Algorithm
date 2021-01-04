import sys; sys.stdin = open('text1.txt', 'r')

# binary_search clear

# from collections import Counter

# def binary_search(temp_arr):
#     # start, end
#     # s, e = 0, max(temp_arr) => 1짜리 케이블만 존재할 때 mid 값 계산에 오류 발생
#     s, e = 0, 2 ** 31

#     while s <= e:
#         temp = 0
#         mid = (s + e) // 2
#         for val, cnt in temp_arr.items():
#             if val // mid:
#                 temp += (val // mid) * cnt
        
#         if temp >= N:
#             res = mid
#             s = mid + 1
#         else:
#             e = mid - 1
    
#     return res


# K, N = map(int, input().split())
# arr = Counter(int(input()) for _ in range(K))

# res = binary_search(arr)
# print(res)


# best solve

# K, N = map(int, input().split())
# arr = [int(input()) for _ in range(K)]
# s, e = 1, sum(arr) // N

# while s <= e:
#     mid = (s + e) // 2
#     cnt = sum([val // mid for val in arr])
#     if cnt < N:
#         e = mid - 1
#     elif cnt >= N:
#         s = mid + 1
#         res = mid
        
# print(res)



# use sys

from sys import stdin

K, N = map(int,stdin.readline().split())
li = list(map(int,stdin.readlines()))

h, l = sum(li)//N, 1
while l <= h :
    mid = (h+l)//2
    cnt = sum([x//mid for x in li])
    if cnt < N:
        h = mid - 1
    elif cnt >= N:
        l = mid + 1
        ans = mid

print(ans)