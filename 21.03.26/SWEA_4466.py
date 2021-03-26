import sys; sys.stdin = open('4466.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))

    answer = 0
    scores.sort(reverse=True)
    for score in scores[:K]:
        answer += score
    print(f'#{tc} {answer}')