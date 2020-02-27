def consult(cnt):
    global maximum
    if cnt == len(select): # 상담 뭐할지 판별 다 했으면 계산시작
        temp = 0           # 이걸로 최대값과 비교할거임
        possible_day = [0] * N  # 그날짜마다 상담이 가능한지 비교 (달력)
        for i in range(len(select)):
            if select[i] == True:  # 상담 가능한 날이다?
                if i + consult_day[i][0] <= len(possible_day): # 근데 그 상담이 퇴사 전이다?
                    for j in range(i, i + consult_day[i][0]): # 달력에 체크 ㄱㄱ
                        if possible_day[j] == 0: # 가능한 날이면
                            possible_day[j] = 1  # 표시
                        else:                    # 상담 날짜가 겹쳤다?
                            return               # 탈출
                else:
                    continue
                temp += consult_day[i][1] # 상담 날짜가 모두 안겹친다면? temp에 값이 더해져있음
        if temp > maximum: # 값 비교해서 max값 변경
            maximum = temp
        return

    select[cnt] = True  # 재
    consult(cnt+1)      # 귀
    select[cnt] = False # 함
    consult(cnt+1)      # 수




N = int(input())
consult_day = [list(map(int, input().split())) for i in range(N)]
select = [False] * N  # 이걸로 어떤 상담 할지 결정
maximum = 0  # 최대값 
consult(0)
print(maximum)



# 다른사람꺼(속도 엄청 빠름)
# n = int(input())
# t=[]
# p=[]
# dp=[]
# for i in range(n):
#     temp_t ,temp_p = map(int,input().split())
#     t.append(temp_t)
#     p.append(temp_p)
#     dp.append(temp_p)

# dp.append(0)

# #print('t',t)
# #print('p',p)

# for i in range(n-1,-1,-1):
#     if t[i]+i>n:
#         dp[i]=dp[i+1]
#     else:
#         dp[i] = max(dp[i+1],p[i]+dp[i+t[i]])

# print(dp[0])