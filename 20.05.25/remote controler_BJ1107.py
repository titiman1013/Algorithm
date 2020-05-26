import sys; sys.stdin = open('remote controler.txt', 'r')

def plus(now):
    global start, end
    temp = 0
    while now != end:
        now += 1
        temp += 1
    
    return temp


def minus(now):
    global start, end
    temp = 0
    while now != end:
        now -= 1
        temp += 1
        if now < 0:
            temp = 10000000
            break
    
    return temp


def press_num(now):
    global start, end
    temp = 0
    now = ''
    for i in range(len(str(end))):
        if int(str(end)[i]) not in ban_list:
            now += str(end)[i]
        else:
            pass


for tc in range(1, int(input())+1):
    start = 100
    end = int(input())
    N = int(input())
    ban_list = list(map(int, input().split()))
    
    res = min(plus(start), minus(start), press_num(start))

    print(f'#{tc} {res}')