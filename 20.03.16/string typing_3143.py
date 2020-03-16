import sys; sys.stdin = open('string typing.txt', 'r')

for tc in range(1, int(input())+1):
    A, B = input().split()
    
    # cnt = 0
    # for i in range(len(A)-len(B)+1):
    #     if A[i:i+len(B)] == B:
    #         cnt += 1
    # print(f'#{tc} {len(A)-cnt*len(B)+cnt}')

    # 중복으로 세는것을 피하려면 for문보다는 while문이 더 좋다!
    cnt = 0
    st = 0 
    while st <= len(A) - len(B):
        if A[st:st+len(B)] == B:
            st += len(B)
            cnt += 1
        else:
            st += 1
    print(f'#{tc} {len(A)-cnt*len(B)+cnt}')