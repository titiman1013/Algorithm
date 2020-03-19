arr = 'ABC'; N = len(arr)
bit = [0] * N

# for 문을 N번 중첩
for i in range(2):
    bit[0] = i
    for i in range(2):
        bit[1] = i
        for i in range(2):
            bit[2] = i
            for j in range(N):
                if bit[j]: print(arr[j], end=' ')
            print()


def subset(k, n):       # k: 함수호출의 깊이, n: 호출트리의 높이, 단말 노드
    if k == n:
        print(bit)
    else:
        bit[k] = 0
        subset(k+1, n)
        bit[k] = 1
        subset(k+1, n)
        # 같은 방법인데 for문 사용
        # for i in range(2):
        #     bit[k] = i
        #     subset(k+1, n)

print(subset(0, 3))