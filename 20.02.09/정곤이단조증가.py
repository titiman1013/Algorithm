def inc_check(num):
    chk = num % 10
    num = int(num/10)
    while num > 0:
        if int(num%10) > chk:
            return False
        else:
            chk = num % 10
            num = int(num/10)
    return True
T = int(input())
for ts in range(1, T+1):
    print('#%d'%ts, end=' ')
    N = int(input())
    nums = list(map(int, input().split()))
    muls = []
    err = -1
    max_mul = -2147000000
    for i in range(N-1):
        for j in range(i+1, N):
            muls.append(nums[i]*nums[j])
    for k in range(len(muls)):
        if inc_check(muls[k]) == False:
            continue
        else:
            err += 1
            if max_mul < muls[k]:
                max_mul = muls[k]
    if err == -1:
        print(-1)
    else:
        print(max_mul)