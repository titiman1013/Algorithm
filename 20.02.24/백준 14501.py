def consult(cnt):
    if cnt == len(possible):
        for i in range(len(possible)):
            if possible[i] == True:
                day += lis[i][0]
        if day > N:
            day = 0
            return
        else:
            sum_ = 0
            for i in range(len(possible)):
                if possible[i] == True:
                    sum_ += lis[i][1]
            
    for i in range(lis[cnt][0]):
        if cnt + i <= len(possible):
            possible[cnt+i] = True
    consult(cnt+1)
    for i in range(lis[cnt][0]):
        if cnt + i <= len(possible):
            possible[cnt+i] = False
    consult(cnt+1)




N = int(input())
lis = []
for i in range(N):
    T, P = list(map(int, input().split()))
    lis.append((T ,P))
result = 0
day = 0
cnt = 0
possible = [False] * N
print(possible)
print(lis)