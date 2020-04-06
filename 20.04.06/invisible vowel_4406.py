import sys; sys.stdin = open("invisible vowel.txt", "r")

for tc in range(1, int(input())+1):
    arrs = input()

    res = ''
    for arr in arrs:
        if not (arr == 'a' or arr == 'e' or arr == 'i' or arr == 'o' or arr == 'u'):
            res += arr

    print(f'#{tc} {res}')