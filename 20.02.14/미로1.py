import sys
sys.stdin = open("미로1.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for t in range(10):
    tc = int(input())
    arr = [list(map(int, list(input()))) for i in range(16)]
    stack = [[1,1]]
    result = 0

    while stack:
        i, j = stack.pop()
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if arr[x][y] == 0:
                stack.append([x, y])
            elif arr[i][j] == 3:
                result = 1
                break
        arr[i][j] = 2

    print('#{} {}'.format(t+1, result))




# 진솔이꺼
# def find(x,y,arr):
#     if arr[x][y]=='3':
#         return 1
  
#     elif arr[x][y] == '0':
#         dx=[1,-1,0,0]
#         dy=[0,0,1,-1]
#         arr[x][y] = '2'
#         return find(x+dx[0],y+dy[0],arr)+find(x+dx[1],y+dy[1],arr)+find(x+dx[2],y+dy[2],arr)+find(x+dx[3],y+dy[3],arr)
#     else :
#         return 0
 
# for tc in range(1,11):
#     t = input()
#     arr = [list(input()) for i in range(16)]
#     arr[1][1] = '0'
#     print(f'#{tc} {find(1,1,arr)}')