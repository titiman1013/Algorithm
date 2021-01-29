import sys; sys.stdin = open('text1.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    A = list(map(int, input().split()))
    B, C = map(int, input().split())

    answer = 0
    for room in A:
        answer += 1
        room -= B
        if room > 0:
            if room % C:
                answer += room // C + 1
            else:
                answer += room // C
    
    print(answer)