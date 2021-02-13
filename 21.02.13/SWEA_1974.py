import sys; sys.stdin = open('1974.txt', 'r')

for tc in range(1, int(input()) + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    for i in range(9):
        # 행, 열 검사 한번에 실시
        hor = [False] * 9
        ver = [False] * 9
        for j in range(9):
            # 만약 수가 중복되면 break
            if hor[arr[i][j] - 1] or ver[arr[j][i] - 1]:
                break
            hor[arr[i][j] - 1] = True
            ver[arr[j][i] - 1] = True
        # False가 존재하면 중간에 break됐다는 뜻
        for k in range(9):
            if hor[k] == False or ver[k] == False:
                break
        # break문에 걸리지 않는다면 다음 실행
        else: continue
        # False 유무 판별의 break문에 걸렸다면 break
        break
    # 행, 열 검사를 중복없이 통과했다면 칸 검사 실행
    else:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                # 이미 중복수를 확인했으므로 칸안의 값의 합으로 판별
                cell = 45
                for k in range(3):
                    cell -= sum(arr[i+k][j:j+3])
                # 만약 중복된 수가 칸 안에 들어있다면 45를 다 지우지 못함 break
                if cell: break
            # 합이 45가 됐다면 다음 실행
            else: continue
            # cell의 값이 남아있다면 break문에 걸리고 밑의 break실행
            break
        # 칸의 확인도 다 끝났다면 출력하고 다음 TC를 실행
        else:
            print(f'#{tc} {1}')
            continue
    # 칸 검사에서 실패할 경우
    print(f'#{tc} {0}')