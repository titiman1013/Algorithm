import sys; sys.stdin = open('text1.txt', 'r')

def check(temp_arr):
    temp = 0
    for i in range(N):
        temp += temp_arr[i]
    if temp <= M:
        return temp

    avg = temp // N
    temp_arr.sort()
    temp_lst = []
    upper_lst = []
    for i in range(N):
        if temp_arr[i] <= avg:
            temp_lst.append(temp_arr[i])
        else:
            upper_lst.append(temp_arr[i])
    
    remain_val = M - sum(temp_lst)
    remain_avg = remain_val // len(upper_lst)
    for i in range(len(upper_lst)):
        temp_lst.append(remain_avg)
    print(temp_lst)
    return max(temp_lst)



N = int(input())
arr = list(map(int, input().split()))
M = int(input())

res = check(arr)
print(res)