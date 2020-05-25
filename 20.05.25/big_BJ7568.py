import sys; sys.stdin = open('big.txt', 'r')

arr = []
for N in range(int(input())):
    arr.append(list(map(int, input().split()))+[0])

for i in range(len(arr)):
    n = 0
    for j in range(len(arr)):
        if i == j:
            continue
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            n += 1
    arr[i][2] = n + 1
    print(n + 1, end=' ')
# print()