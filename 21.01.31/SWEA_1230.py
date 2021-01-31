import sys; sys.stdin = open('1230.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    passwords = list(map(int, input().split()))
    M = int(input())
    orders = list(map(str, input().split()))