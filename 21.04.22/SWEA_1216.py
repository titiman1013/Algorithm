import sys; sys.stdin = open('1216.txt', 'r')

for tc in range(1, 11):
    answer = 0

    T = int(input())
    arr = list(input() for _ in range(100))