import sys
sys.stdin = open("시험점수.txt", "r")

def _sum(cnt):
    if cnt == N:
        temp = 0
        for i in range(N):
            if check[i] == True:
                temp += score[i]
        result.add(temp)
        return
    
    check[cnt] = True
    _sum(cnt+1)
    check[cnt] = False
    _sum(cnt+1)





T = int(input())
for t in range(T):
    N = int(input())
    score = list(map(int, input().split()))
    result = set()
    check = [False] * N
    _sum(0)
    print(f'#{t+1} {len(result)}')