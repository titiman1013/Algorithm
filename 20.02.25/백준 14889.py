def search(cnt):
    global result
    if cnt == len(check):  # 모든 요소 True/False 로 뽑기 => 팀 나누기
        temp = 0
        for i in range(len(check)): # True 값 세주기
            if check[i] == True:
                temp += 1
        if temp == N//2: # 반으로 나눴을 때 값을 체크
            a_list = []
            b_list = []
            a_team = 0
            b_team = 0
            for i in range(len(check)): # a팀 누구누군지
                if check[i] == True:
                    a_list.append(i)
                else:                   # b팀 누구누군지
                    b_list.append(i)
            for i in a_list:
                for j in a_list:
                    if i != j:
                        a_team += arr[i][j] # a팀 시너지합
            for i in b_list:
                for j in b_list:
                    if i != j:
                        b_team += arr[i][j] # b팀 시너지합
            if abs(a_team - b_team) < result: # 각 팀의 합의 차 계산해서 결과값에 최솟값 저장
                result = abs(a_team - b_team)

        return 

    check[cnt] = True  # 재
    search(cnt+1)      # 귀
    check[cnt] = False # 함
    search(cnt+1)      # 수




N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]

cnt = 0
check = [False] * N
result = 100000

search(0)
print(result)