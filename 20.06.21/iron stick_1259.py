import sys; sys.stdin = open('iron stick.txt', 'r')

def search(ss):
    while True:
        if ss[-1] in screw_temp:
            for ind, val in enumerate(screw_temp):
                if ss[-1] == val and ind % 2 == 0:
                    ss.append(screw_temp[ind])
                    ss.append(screw_temp[ind+1])
                    screw_temp.pop(ind+1)
                    screw_temp.pop(ind)
                    break
        if ss[-1] not in screw_temp:
           return ss
  
  
  
T=int(input())
for tc in range(1, T+1):
    n = int(input())
    screw = list(map(int,input().split()))
    max_number = 0
    last_result = []
    for i in range(len(screw)//2):
        ss=screw[2*i:2*i+2]
        screw_temp=screw[:]
        screw_temp.pop(2*i+1)
        screw_temp.pop(2*i)
        result=search(ss)
        if max_number<len(result):
            last_result=result[:]
            max_number=len(result)
    print('#{} '.format(tc), end='')
    for iii in last_result:
        print(iii, end=' ')
    print('')