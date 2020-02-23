T = int(input())
for t in range(T):
    arr = [list(map(int, input().split())) for i in range(9)]
    result = []
    for i in range(9): # 가로줄 판단
        sum_lis = []
        for j in range(9): 
            sum_lis.append(arr[i][j]) 
        if sum(sum_lis) != 45:
            result.append('1')
            break
    for i in range(9): # 세로줄 판단  
        sum_lis.clear() 
        for j in range(9): 
            sum_lis.append(arr[j][i])
        if sum(sum_lis) != 45:
            result.append('1')
            break
    for k in range(3): # 3x3 판단
        sum_lis.clear()
        for i in range(3):     
            for j in range(3):
                sum_lis.append(arr[i+k*3][j+k*3])
        if sum(sum_lis) != 45:
            result.append('1')
 
    if '1' in result:
        print(f'#{t+1} 0')
    else:
        print(f'#{t+1} 1')
