import sys; sys.stdin = open("two number sum.txt", "r")

# for tc in range(1, int(input())+1):
#     A, B = map(int, input().split())

#     print(f'#{tc} {A+B}')


#
T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    lenA = len(A)
    lenB = len(B)
    stack = []
    i = lenA - 1    # A의 index 가장 오른쪽 자리 수
    j = lenB - 1    # B의 index 가장 오른쪽 자리 수
    carry = 0       # 자리올림 수
    while i >= 0 and j >= 0:
        s = int(A[i]) + int(B[j]) + carry
        carry = s // 10
        stack.append(s%10)
        i -= 1
        j -= 1
    while i >= 0:
        s = int(A[i]) + carry
        carry = s // 10
        stack.append(s%10)
        i -= 1
    while j >= 0:
        s = int(B[j]) + carry
        carry = s // 10
        stack.append(s%10)
        j -= 1
    if carry != 0:
        stack.append(carry)

    print('#{} '.format(tc), end='')
    while stack:
        print(stack.pop(), end='')
    print()