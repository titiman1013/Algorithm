import sys; sys.stdin = open('Base64 Decoder.txt', 'r')

from base64 import b64decode

for tc in range(1, int(input())+1):
    arr = input()
    print(f'#{tc} {b64decode(arr).decode("UTF-8")}')


# for tc in range(1, int(input())+1):
#     19 6 37 38 25
#     11 34 31 30