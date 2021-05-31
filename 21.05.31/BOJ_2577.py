import sys; sys.stdin = open('2577.txt', 'r')

from collections import Counter

A = int(input())
B = int(input())
C = int(input())

answer = Counter(str(A * B * C))
for i in range(10):
    if answer.get(str(i)):
        print(answer.get(str(i)))
    else:
        print(0)