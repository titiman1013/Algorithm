import sys; sys.stdin = open('2493.txt', 'r')

import sys

input = sys.stdin.readline

N = int(input().strip('\n'))
heights = list(map(int, input().split()))

answer = []
stack = []
for idx, height in enumerate(heights):
    while stack and heights[stack[-1]] < height:
        stack.pop()

    if stack:
        answer.append(stack[-1] + 1)
    else:
        answer.append(0)

    stack.append(idx)

print(*answer)