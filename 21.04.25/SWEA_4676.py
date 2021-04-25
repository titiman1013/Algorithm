import sys; sys.stdin = open('4676.txt', 'r')

for tc in range(1, int(input()) + 1):
    strings = input()
    H = int(input())
    positions = list(map(int, input().split()))
    answer = ''