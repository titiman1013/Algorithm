import sys
sys.stdin = open('숫자만들기.txt','r')
def f(n,k,r,op1,op2,op3,op4):
    global minV, maxV
    if n==k:
        if maxV<r:
            maxV = r
        if minV>r:
            minV = r
    else:
        if op1>0:
            f(n+1, k, r+card[n], op1-1, op2, op3, op4)
        if op2>0:
            f(n+1, k, r-card[n], op1, op2-1, op3, op4)
        if op3>0:
            f(n+1, k, r*card[n], op1, op2, op3-1, op4)
        if op4>0:
            f(n+1, k, int(r/card[n]), op1, op2, op3, op4-1)
        
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    op1,op2,op3,op4 = map(int,input().split())
    card = list(map(int, input().split()))
    minV = 100000000
    maxV = -100000000
    f(1,N,card[0],op1,op2,op3,op4)
    print('#{} {}'.format(tc, maxV- minV))
