import sys
sys.stdin = open("숫자이어붙이기.txt", "r")

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def search(cnt, x, y, num):
#     if cnt == 7:
#         result.add(num)
#     else:
#         num += str(arr[x][y])
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < 4 and 0 <= ny < 4:
#                 search(cnt+1, nx, ny, num)




# T = int(input())
# for t in range(T):
#     arr = [list(map(int, input().split())) for i in range(4)]
#     result = set()
    
#     for i in range(4):
#         for j in range(4):
#             num = ''
#             search(0, i, j, num)

#     print(f'#{t+1} {len(result)}')




dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def search(cnt, x, y, num):
    if cnt == 7:
        result.add(num)
    else:
        num = num * 10 + arr[x][y]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 4 and 0 <= ny < 4:
                search(cnt+1, nx, ny, num)




T = int(input())
for t in range(T):
    arr = [list(map(int, input().split())) for i in range(4)]
    result = set()
    
    for i in range(4):
        for j in range(4):
            search(0, i, j, num=0)

    print(f'#{t+1} {len(result)}')