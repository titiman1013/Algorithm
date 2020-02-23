import sys
sys.stdin = open("미로.txt", "r")

for T in range(10):
    t = int(input())
    # arr = [input() for i in range(16)]
    arr = []
    # for i in range(16):
    arr.append(input())
    print(arr)
    # for i in range(16):
    #     for j in range(16):
    #         if arr[i][j] == 2:
    #             start = [i, j]
    # print(start)