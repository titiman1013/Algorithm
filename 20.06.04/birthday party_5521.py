import sys; sys.stdin = open('birthday party.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    
    res = 0
    invite = []
    for i in range(len(arr)):
        if arr[i][0] == 1:
            invite.append(arr[i][1])
            res += 1
        elif arr[i][1] == 1:
            invite.append(arr[i][0])
            res += 1

    # print(invite)

    for i in range(len(invite)):
        for j in range(len(arr)):
            if invite[i] == arr[j][0]:
                if arr[j][1] not in invite and arr[j][1] != 1:
                    invite.append(arr[j][1])
                    res += 1
            elif invite[i] == arr[j][1]:
                if arr[j][0] not in invite and arr[j][0] != 1:
                    invite.append(arr[j][0])
                    res += 1
    
    # print(invite)

    print(f'#{tc} {res}')