import sys; sys.stdin = open('1983.txt', 'r')

grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for tc in range(1, int(input()) + 1):
    # N: 학생수, K: 학생 번호
    N, K = map(int, input().split())
    scores = [list(map(int, input().split())) for _ in range(N)]