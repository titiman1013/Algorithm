import sys; sys.stdin = open('procession search.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    box_num = 0
    box_size = []

    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                box_num += 1
                ver = 1     # 수직길이
                hor = 1     # 수평길이

                # 세로
                while arr[i+ver][j]:
                    ver += 1
                # 가로
                while arr[i][j+hor]:
                    hor += 1

                # 지나간곳 삭제
                for x in range(i, i+ver):
                    for y in range(j, j+hor):
                        arr[x][y] = 0
                
                box_size.append([ver*hor, ver, hor])
    
    # 크기별로 정렬
    for k in range(len(box_size)):
        for i in range(len(box_size) - 1):
            if box_size[i][0] < box_size[i+1][0]:
                continue
            elif box_size[i][0] == box_size[i+1][0]:
                if box_size[i][1] < box_size[i+1][1]:
                    continue
            box_size[i], box_size[i+1] = box_size[i+1], box_size[i]


    print(f'#{tc} {box_num}', end=" ")
    for i in range(len(box_size)):
        print(f'{box_size[i][1]} {box_size[i][2]}', end=" ")
    print()