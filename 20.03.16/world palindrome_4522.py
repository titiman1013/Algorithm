import sys; sys.stdin = open('world palindrome.txt', 'r')

for tc in range(1, int(input())+1):
    arr = input()
    print(f'#{tc}', end=' ')
    cnt = 0
    for i in range(len(arr)//2):
        if arr[i] == arr[-1-i]:
            cnt += 1
        elif arr[i] == '?' or arr[-1-i] == '?':
            cnt += 1
    
    if cnt == len(arr) // 2:
        print('Exist')
    else:
        print('Not exist')