import sys; sys.stdin = open('1227.txt', 'r')

for _ in range(10):
    tc = int(input())
    maze = list(input() for _ in range(100))
    answer = 0