import sys; sys.stdin = open('run.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    # N: 사람수, M: 정보개수
    arr = [list(map(int, input().split())) for _ in range(M)]
