import sys; sys.stdin = open('text1.txt', 'r')
import math

def check(num):
    if num == 1: return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0: return False
    return True



for tc in range(1, int(input()) + 1):
    M, N = map(int, input().split())
    for num in range(M, N + 1):
        if check(num):
            print(num)