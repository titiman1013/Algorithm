import sys; sys.stdin = open('9466.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    preferences = [0] + list(map(int, input().split()))

    # pre_dicts = [[str(idx+1), pre] for idx, pre in enumerate(preferences)]
    
    # res = 0
    # while preferences:
    #     num = preferences.pop()
    #     temp = 1
    #     if selected[num] == False:


    # 연결된 것들은 -1로 확인
    selected = [0] * (N + 1)
    team_num = 1
    for i in range(1, N + 1):
        if selected[i] == 0:
            while selected[i] == 0:
                selected[i] = team_num
                i = preferences[i]
            while selected[i] == team_num:
                selected[i] = -1
                i = preferences[i]
            team_num += 1
    
    answer = N - selected.count(-1)
    print(answer)





# answer
# 3
# 0