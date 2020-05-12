import sys; sys.stdin = open('gear.txt', 'r')

for tc in range(1, int(input())+1):
    arr = [list(input()) for _ in range(4)]
    K = int(input())
    solution = [list(map(int, input().split())) for _ in range(K)]
