import sys; sys.stdin = open('text1.txt', 'r')

def check(temp_arr):
    res_lst = []
    for i in range(N):
        visited = [0] * N
        # if visited[i] == 0:
        visited[i] = 1
        temp_lst = [i + 1, temp_arr[i]]
        stack = [temp_arr[i] - 1]
        while stack:
            x = stack.pop()
            for k in range(N):
                if x == k:
                    if visited[x] == 0:
                        visited[x] = 1
                        temp_lst.append(temp_arr[k])
                        stack.append(temp_arr[k] - 1)
        if temp_lst[0] == temp_lst[-1]:
            for val in temp_lst:
                if val not in res_lst:
                    res_lst.append(val)
    return len(res_lst), res_lst



N = int(input())
arr = [int(input()) for _ in range(N)]

res, res_lst = check(arr)
print(res)
for res_val in res_lst:
    print(res_val)