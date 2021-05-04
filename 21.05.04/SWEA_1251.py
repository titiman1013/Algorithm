import sys; sys.stdin = open('1251.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    Xs = list(map(int, input().split()))
    Ys = list(map(int, input().split()))
    E = float(input())