import sys; sys.stdin = open('11758.txt', 'r')

def ccw(p1, p2, p3):
    x1, y1 = p1
    x2 ,y2 = p2
    x3, y3 = p3
    return (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)



for tc in range(1, int(input()) + 1):
    arr = [list(map(int, input().split())) for _ in range(3)]
    
    answer = ccw(*arr)

    if answer < 0:
        print(-1)
    elif answer > 0:
        print(1)
    else:
        print(0)





# answer
# -1
# 0
# 1