import sys; sys.stdin = open('othello.txt', 'r')

import copy

mx = [0, 0, -1, 1, -1, -1, 1, 1]
my = [1, -1, 0, 0, -1, 1, 1, -1]

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    bg = []
    for i in range(n + 2):
        temp = []
        for j in range(n + 2):
            if i == 0 or i == n + 1 or j == 0 or j == n + 1:
                temp.append(-1)
            else:
                temp.append(0)
        bg.append(temp)
    bg[n//2][n//2], bg[n//2+1][n//2+1] = 2, 2
    bg[n//2][n//2+1], bg[n//2+1][n// 2] = 1, 1
    for i in range(m):
        startx, starty, c = map (int, input().split())
        x = startx
        y = starty
        if c == 1:
            bg[y][x] = c
  
            for j in range(len(mx)):
                temp = copy.deepcopy(bg)
                x = startx
                y = starty
                while(True):
                    if bg[y+my[j]][x+mx[j]] == 2:
                        bg[y + my[j]][x + mx[j]] = c
                        x = x + mx[j]
                        y = y + my[j]
                    elif bg[y+my[j]][x+mx[j]] == -1:
                        bg = temp
                        break
                    elif bg[y+my[j]][x+mx[j]] == 0:
                        bg = temp
                        break
                    elif bg[y+my[j]][x+mx[j]] == 1:
                        break
        else:
            bg[y][x] = c
  
            for j in range(len(mx)):
                temp = copy.deepcopy(bg)
                x = startx
                y = starty
                while(True):
                    if bg[y+my[j]][x+mx[j]] == 1:
                        bg[y+my[j]][x+mx[j]] = c
                        x = x + mx[j]
                        y = y + my[j]
                    elif bg[y+my[j]][x+mx[j]] == -1:
                        bg = temp
                        break
                    elif bg[y+my[j]][x+mx[j]] == 0:
                        bg = temp
                        break
                    elif bg[y+my[j]][x+mx[j]] == 2:
                        break
  
    cnt1 = 0
    cnt2 = 0
    for i in bg:
        cnt1 += i.count(1)
        cnt2 += i.count(2)

    print(f'#{t} {cnt1} {cnt2}')