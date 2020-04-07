import sys; sys.stdin = open("Digit sum.txt", "r")

# for tc in range(1, int(input())+1):
#     n = int(input())
    
#     res = 0
#     while True:
#         if n < 10: 
#             res += n
#             if res < 10:
#                 break
#             else:
#                 n = res
#                 res = 0
#         res += n % 10
#         n -= n % 10
#         n //= 10
#     print(f'#{tc} {res}')

# for tc in range(1, int(input())+1):
#     n = input()
    
#     res = 0
#     while True:    
#         for i in range(len(n)):
#             res += int(n[i])
#         if res < 10:
#             break
#         else:
#             n = str(res)
#             res = 0

#     print(f'#{tc} {res}')

for tc in range(1, int(input())+1):
    n = input()

    res = 0
    if len(n) == 1:
        res = int(n[0])
    else:
        res = int(n[-1]) + 1
    print(f'#{tc} {res}')