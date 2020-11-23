import sys; sys.stdin = open('text2.txt', 'r')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

grade = [0 for i in range(N)]
for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j: continue;
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            grade[i] += 1
for i in range(len(grade)):
    print(grade[i] + 1, end=" ")