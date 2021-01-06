import sys; sys.stdin = open('text1.txt', 'r')

def binary_search(temp_arr):
    s, e = 1, temp_arr[-1] - temp_arr[0]
    res = 0

    while s <= e:
        mid = (s + e) // 2
        cnt = 1
        pre_house = temp_arr[0]
        for i in range(1, N):
            if pre_house + mid <= temp_arr[i]:
                pre_house = temp_arr[i]
                cnt += 1
        
        if cnt >= C:
            res = mid
            s = mid + 1
        else:
            e = mid - 1
    return res



N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]

arr.sort()
res = binary_search(arr)
print(res)