# 기본 재귀호출 factorial

def f(n):
    global res
    if n == 1:
        return
    
    res *= n
    f(n-1)
    return res

res = 1
print(f(5))


# 재귀함수는 기본적으로 반복적 작업
# for, while 없이 가능

# for i in range(3):
#     print('Hello!!!!')

def printHello(i):
    if i == 3:
        return
    print('Hello!!!!')
    printHello(i+1)

printHello(0)


# 가지치기를 해나간다 할때 끝 가지의 갯수
def func(i, n):
    if i == n:
        global cnt;
        cnt += 1
        return

    func(i+1, n)
    func(i+1, n)

cnt = 0
func(0, 3)
print('cnt =', cnt)