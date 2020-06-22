import sys; sys.stdin = open('sum.txt', 'r')

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
 
for n in range(10):
    T = int(input())
    numbers = [list(map(int, input().split())) for n in range(100)]
 
    a_list = []
    for i in range(100):
        a=0 #가로
        for j in range(100):
            a+=numbers[i][j]
        a_list.append(a)
 
    b_list = []
    for j in range(100):
        b=0 #세로
        for i in range(100):
            b+=numbers[i][j]
        b_list.append(b)
     
    c_list=[]
    for i in range(100):
        c=0 #오밑대각
        for j in range(100):
            if i==j:
                c+=numbers[i][j]
        c_list.append(c)
 
    d_list=[]
    for j in range(100):
        d=0 #왼밑대각
        for i in range(100):
            if j==i:
                d+=numbers[i][j]
        d_list.append(d)
     
    a_max = max(a_list)
    b_max = max(b_list)
    c_max = max(c_list)
    d_max = max(d_list)
    MAX = [a_max, b_max, c_max, d_max]
    result = max(MAX)
    print(f'#{T} {result}')

