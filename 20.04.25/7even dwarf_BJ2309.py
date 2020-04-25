import sys; sys.stdin = open('7even dwarf.txt', 'r')


def discriminator(cnt, head_cnt, height_sum):
    if res:
        return
    if cnt == 9:
        if head_cnt == 7 and height_sum == 100:
            for i in range(len(check)):
                if check[i] == True:
                    res.append(arr[i])
            # print(check)
        return

    check[cnt] = True
    discriminator(cnt+1, head_cnt+1, height_sum+arr[cnt])
    check[cnt] = False
    discriminator(cnt+1, head_cnt, height_sum)


for tc in range(1, int(input())+1):
    arr = [int(input()) for _ in range(9)] 
    check = [False] * 9
    res = []
    discriminator(0, 0, 0)
    res.sort()

    # print(f'#{tc}', end= ' ')
    # for i in range(len(res)):
    #     print(res[i], end=' ')
    # print()

    for i in range(len(res)):
        print(res[i])


# 답
# 7
# 8
# 10
# 13
# 19
# 20
# 23