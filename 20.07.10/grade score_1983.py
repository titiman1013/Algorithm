import sys; sys.stdin = open('grade score.txt', 'r')


for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    # N: 학생 수, K: 점수 확인하는 학생 idx
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 총점 = 35% + 45% + 20%
    # 평가는 열개중 N/10명을 동일하게 부여
    # A+ A0 A- B+ B0 B- C+ C0 C- D0

    scores = [[0] for _ in range(N)]
    for i in range(N):
        scores[i] = (arr[i][0] * 0.35 + arr[i][1] * 0.45 + arr[i][2] * 0.2) * 100
    
    # print(scores)
    print(arr)