import sys; sys.stdin = open('where string insert.txt', 'r')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())  
    m=list()
    for i in range(0,n) :
        l=map(int, input().split())
        m.append(list(l))
    ans=0
    for i in range(0,n) :
        c=0;
        for j in range(0,n) :
            if m[i][j] == 1:
                c=c+1
            else :
                if c==k :
                    ans=ans+1
                c=0
        if c==k :
            ans=ans+1
    for i in range(0,n) :
        c=0;
        for j in range(0,n) :
            if m[j][i]== 1:
                c=c+1
            else :
                if c==k :
                    ans=ans+1
                c=0 
        if c==k :
            ans=ans+1
    print('#%d %d'%(test_case, ans))
