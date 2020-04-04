import sys; sys.stdin = open("speedy phone keypad.txt", "r")

for tc in range(1, int(input())+1):
    S, N = map(int, input().split())    # S는 문자번호화 N은 단어의 개수
    arrs = list(input().split())     # 단어장 단어목록

    # 1                # 2(a, b, c)    # 3(d, e, f)    
    # 4(g, h, i)       # 5(j, k, l)    # 6(m, n, o)
    # 7(p, q, r, s)    # 8(t, u, v)    # 9(w, x, y, z)

    res = 0
    for arr in arrs:
        temp = ''
        for i in range(len(arr)):
            if arr[i] == 'a' or arr[i] == 'b' or arr[i] == 'c':
                temp += '2'
            elif arr[i] == 'd' or arr[i] == 'e' or arr[i] == 'f':
                temp += '3'
            elif arr[i] == 'g' or arr[i] == 'h' or arr[i] == 'i':
                temp += '4'
            elif arr[i] == 'j' or arr[i] == 'k' or arr[i] == 'l':
                temp += '5'
            elif arr[i] == 'm' or arr[i] == 'n' or arr[i] == 'o':
                temp += '6'
            elif arr[i] == 'p' or arr[i] == 'q' or arr[i] == 'r' or arr[i] == 's':
                temp += '7'
            elif arr[i] == 't' or arr[i] == 'u' or arr[i] == 'v':
                temp += '8'
            elif arr[i] == 'w' or arr[i] == 'x' or arr[i] == 'y' or arr[i] == 'z':
                temp += '9'
        if int(temp) == S:
            res += 1
    
    print(f'#{tc} {res}')