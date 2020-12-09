import sys; sys.stdin = open('text1.txt', 'r')

for tc in range(int(input())):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    
    