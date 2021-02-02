import sys; sys.stdin = open('1209.txt', 'r')

for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]