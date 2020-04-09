import sys; sys.stdin = open("number insert.txt", "r")

for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))
    insert_number = []
    for i in range(M):
        insert_number.append(list(map(int, input().split())))

    for i in insert_number:
        arr.insert(i[0], i[1])
        
    print(f'#{tc} {arr[L]}')