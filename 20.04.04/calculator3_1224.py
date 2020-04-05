import sys; sys.stdin = open("calculator3.txt", "r")

for tc in range(1, 11):
    tc_length = int(input())
    arrs = input()
    
    # stack
    number = []
    operator = []
    for arr in arrs:
        if arr.isdecimal():
            number.append(arr)
        else:
            