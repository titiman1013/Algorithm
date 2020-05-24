import sys; sys.stdin = open('password creation.txt', 'r')

for t in range(10):
    T = int(input())
    nums = list(map(int, input().split()))
 
    print(f'#{T}', end = " ")
 
    n = 1
    while True:
        a = nums.pop(0) - n
        if a <= 0:
            a = 0
            nums.append(a)
            break
        else:
            nums.append(a)
        n += 1
        if n == 6:
            n = 1
    for i in nums:
        print(f'{i}', end = " ")
    print()