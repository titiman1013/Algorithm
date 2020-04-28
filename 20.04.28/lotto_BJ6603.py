import sys; sys.stdin = open('lotto.txt', 'r')

from itertools import combinations

a = 0
while True:
    nums = list(map(int, input().split()))
    k = nums.pop(0)
    if len(nums) == 0 and k == 0:
        break
    if a != 0:    
        print()
    for pick in list(combinations(nums, 6)):
        for i in range(len(pick)):
            print(pick[i], end=' ')
        print()
    a += 1