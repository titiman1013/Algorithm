import sys; sys.stdin = open('1107.txt', 'r')

import sys

for tc in range(1, int(input()) + 1):
    input = sys.stdin.readline
    N = int(input())
    M = int(input())
    if M > 0:
        errors = list(map(int, input().split()))
    else:
        errors = []
    
    answer = abs(N - 100)
    for channel in range(1000001):
        for num in str(channel):
            if int(num) in errors: break
        else:
            answer = min(answer, abs(channel - N) + len(str(channel)))

    print(answer)