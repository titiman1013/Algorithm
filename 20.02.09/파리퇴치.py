T = int(input())
for t in range(T):
    NM = list(map(int, input().split()))
    flys = [list(map(int, input().split())) for i in range(NM[0])]
 
    max_flys = []
    stick = NM[1]
    for i in range(NM[0]-stick+1):
        for j in range(NM[0]-stick+1):
            flies = 0
            for m in range(stick):
                for n in range(stick):
                    flies += flys[i+m][j+n]
            max_flys.append(flies)
     
         
    print(f'#{t+1} {max(max_flys)}')
