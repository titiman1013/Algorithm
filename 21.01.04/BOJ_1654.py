import sys; sys.stdin = open('text1.txt', 'r')
from collections import Counter

def binary_search(temp_arr):
    # start, end
    # s, e = 0, max(temp_arr)
    s, e = 0, 2 ** 31

    while s <= e:
        temp = 0
        mid = (s + e) // 2
        for val, cnt in temp_arr.items():
            if val // mid:
                temp += (val // mid) * cnt
        
        if temp >= N:
            res = mid
            s = mid + 1
        else:
            e = mid - 1
    
    return res


K, N = map(int, input().split())
arr = Counter(int(input()) for _ in range(K))

res = binary_search(arr)
print(res)