import sys; sys.stdin = open('1217.txt', 'r')

def reculsive(N, M, res):
    global answer

    if M == 0:
        answer = res
        return
    
    reculsive(N, M - 1, res * N)



for _ in range(1, 11):
    tc = int(input())
    N, M = map(int, input().split())

    answer = 0 
    reculsive(N, M, 1)
    print(f'#{tc} {answer}')