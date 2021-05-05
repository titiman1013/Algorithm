import sys; sys.stdin = open('1210.txt', 'r')

for _ in range(1, 11):
    tc = int(input())
    ladders = list(list(map(int, input().split())) for _ in range(100))