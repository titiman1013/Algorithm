import sys; sys.stdin = open("runner.txt", "r")

# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input(). split())) for _ in range(M)]
    




#
from math import factorial as f
MOD = 10**6+3
 
def solve(flag):
    if flag == full:
        return 1
 
    if dp[flag] != -1:
        return dp[flag]
    dp[flag] = 0
 
    for i in range(n):
        if (flag & 1<<i) == 0 and (flag & needs[i]) == needs[i]:
            dp[flag] += solve(flag | 1<<i)
    return dp[flag]
 
for T in range(1,int(input())+1):    
    n,m = map(int,input().split())
    needs = [0]*16
    dp = [-1]*(1<<n)
 
    for i in range(m):
        a,b = map(int,input().split())
        needs[b-1] |= 1<<(a-1)
    full = (1<<n)-1    
    print('#%d %d' %(T,solve(0)))


# ##
# from math import factorial as f
# MOD = 10**6+3
 
# def solve(flag):
#     if flag == full:
#         return 1
 
#     if dp[flag] != -1:
#         return dp[flag]
#     dp[flag] = 0
 
#     for i in range(n):
#         if (flag & 1<<i) == 0 and (flag & needs[i]) == needs[i]:
#             dp[flag] += solve(flag | 1<<i)
#     return dp[flag]
 
# for T in range(1,int(input())+1):
#     n,m = map(int,input().split())
 
#     g = [-1] * 31
#     adj = [list(map(int, input().split())) for i in range(m)]
#     parent = [[] for i in range(n+1)]
#     cnt = 0
#     for a,b in adj:
#         parent[b] += [a]
#         if g[a] == g[b] == -1: g[a] = g[b] = cnt; cnt += 1
#         elif g[a] == -1: g[a] = g[b]
#         elif g[b] == -1: g[b] = g[a]
#         else:
#             idx = g[b]
#             for i in range(n+1):
#                 if g[i] == idx: g[i] = g[a]
 
#     glist = [[] for i in range(cnt+1)]
#     for i in range(1,n+1):
#         glist[g[i]+1] += [i]
 
#     res = [(len(glist[0]), f(len(glist[0])))]
#     for i in range(1,cnt+1):
#         dp = [-1]*(1<<16)
#         index = [-1]*31
#         needs = [0]*16
 
#         c = 0
#         for j in glist[i]:
#             index[j] = c; c+=1
     
#         for j in glist[i]:
#             for p in parent[j]:   
#                 needs[index[j]] |= 1<<index[p]
#         l = len(glist[i])
#         full = (1<<l)-1
#         res += [(l, solve(0))]
 
#     ans = f(n)
#     cnt = 0
#     for a,b in res:
#         if a != 0:        
#             ans //= f(a)
#     for a,b in res:
#         ans *= b
#     print('#%d %d' %(T,ans))
