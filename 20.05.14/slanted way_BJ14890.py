import sys; sys.stdin = open('slanted way.txt', 'r')

for tc in range(1, int(input())+1):
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    res = 0
    # 가로
    for i in range(N):
        slant = 0
        cnt = 0
        flat = 0
        for j in range(N):
            if j == 0:    # 처음 땅높이
                slant = arr[i][j]
                flat += 1
            else:       # 처음이 아닐때
                if arr[i][j] != slant:      # 경사가 생길때
                    if cnt: 
                        # print('break', i, j)
                        break       # 이미 경사진길 상태이면 break
                    else:       # 경사진길을 만날때
                        if abs(slant - arr[i][j]) != 1:      # 땅높이가 2이상 차이나면 break
                            # print('break', i, j)
                            break
                        else:       # 정상적인 경사일때 갯수 세주기 시작
                            if arr[i][j] - slant > 0:       # 경사가 오르막이면
                                if flat < L:
                                    # print(flat)
                                    # print('break', i, j)
                                    break
                                else:
                                    flat = 1
                                    slant = arr[i][j]
                            else:       # 경사가 내리막이면
                                slant = arr[i][j]
                                cnt += 1
                                if cnt == L:
                                    cnt = 0
                                    flat = 0
                else:
                    if cnt:     # 경사면 일때
                        cnt += 1
                        if cnt == L:
                            cnt = 0
                            flat = 0
                    else:       # 평지일때
                        flat += 1
        else:       # 스무스하게 지나오면
            if cnt:
                continue
            res += 1
    #         print(i)
    # print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
    
    # 세로
    for i in range(N):
        slant = 0
        cnt = 0
        flat = 0
        for j in range(N):
            if j == 0:    
                slant = arr[j][i]
                flat += 1
            else:       
                if arr[j][i] != slant:     
                    if cnt: 
                        # print('break', i, j)
                        break       
                    else:    
                        if abs(slant - arr[j][i]) != 1:    
                            # print('break', i, j)
                            break
                        else:      
                            if arr[j][i] - slant > 0:
                                if flat < L:
                                    # print('break', i, j)
                                    break
                                else:
                                    flat = 1
                                    slant = arr[j][i]
                            else:
                                slant = arr[j][i]
                                cnt += 1
                                if cnt == L:
                                    cnt = 0
                                    flat = 0
                else:
                    if cnt:
                        cnt += 1
                        if cnt == L:
                            cnt = 0
                            flat = 0
                    else:
                        flat += 1
        else:    
            if cnt:
                continue
            res += 1
            # print(i)

    print(f'#{tc} {res}')
# print(abs(2-3))

# 반례 답
# 10
# 2
# 2
# 7
# 7
# 1
# 5
# 5
# 6
# 4

# 반례2 답
# 11
# 6
# 4
# 6
# 4
# 11
# 10
# 11
# 10
# 3
# 5
# 1
# 8
# 5
# 10
# 7
# 5
# 4
# 10

# 반례3 답
# 3
# 2
# 1
# 9
# 16