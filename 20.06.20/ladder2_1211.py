import sys; sys.stdin = open('ladder2.txt', 'r')

for t in range(10):
    T = int(input())
    ladders = [list(map(int, input().split())) for i in range(100)]
 
    X = 0
    MIN = 100000
    for j in range(100): # 가로로 움직여서 입구찾기
        if ladders[0][j] == 1:
            x = j
            cnt = 0
 
        for i in range(100):
            if x != 0 and ladders[i][x - 1] == 1:
                while x != 0 and ladders[i][x - 1] == 1 :
                    x -= 1
                    cnt += 1
            elif x < 99 and ladders[i][x + 1] == 1:
                while x != 99 and ladders[i][x + 1] == 1:
                    x += 1
                    cnt += 1
         
        if cnt < MIN:
            MIN = cnt
            X = j 
    print(f'#{t+1} {X}')
