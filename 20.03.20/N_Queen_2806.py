import sys; sys.stdin = open('N_Queen.txt', 'r')

T=int(input())
def backtracking(x):
    global cnt
    for i in range(x+1):
        if x!=i:
            if (visited[i]==visited[x]) or (abs(visited[i]-visited[x])==abs(i-x)):
                return
    if x==N-1:
        cnt+=1
        return
    for i in range(N):
        visited[x+1]=i
        backtracking(x+1)
 
 
 
 
for tc in range(1,T+1):
    N=int(input())
    cnt=0
    visited=[-1]*11
    for i in range(N):
        visited[0]=i
        backtracking(0)
 
    print('#{} {}'.format(tc,cnt))
