import sys; sys.stdin = open('1983.txt', 'r')

grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for tc in range(1, int(input()) + 1):
    # N: 학생수, K: 학생 번호
    N, K = map(int, input().split())
    # scores = [list(map(int, input().split())) for _ in range(N)]

    scores = []
    idx = 1
    for _ in range(N):
        mid, fin, rep = map(int, input().split())
        scores.append([mid * 0.35 + fin * 0.45 + rep * 0.2, idx])
        idx += 1

    scores.sort(reverse=True)
    for idx, student in enumerate(scores):
        if student[1] == K:
            break
    
    tmp = N // 10
    if (idx + 1) % tmp:
        print(f'#{tc} {grades[(idx + 1) // tmp]}')
    else:
        print(f'#{tc} {grades[(idx + 1) // tmp - 1]}')