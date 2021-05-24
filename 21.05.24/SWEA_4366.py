import sys; sys.stdin = open('4366.txt', 'r')

for tc in range(1, int(input()) + 1):
    binarys = input()
    trinarys = input()

    sub_set = set()
    for idx, binary in enumerate(binarys):
        if idx == 0: continue
        else:
            if binary == '1':
                tmp = int(binarys[:idx] + '0' + binarys[idx + 1:], 2)
            else:
                tmp = int(binarys[:idx] + '1' + binarys[idx + 1:], 2)
            sub_set.add(tmp)
    
    for idx, trinary in enumerate(trinarys):
        if trinary == '0':
            tmp1 = int(trinarys[:idx] + '1' + trinarys[idx + 1:], 3)
            tmp2 = int(trinarys[:idx] + '2' + trinarys[idx + 1:], 3)
        elif trinary == '1':
            tmp1 = int(trinarys[:idx] + '0' + trinarys[idx + 1:], 3)
            tmp2 = int(trinarys[:idx] + '2' + trinarys[idx + 1:], 3)
        else:
            tmp1 = int(trinarys[:idx] + '0' + trinarys[idx + 1:], 3)
            tmp2 = int(trinarys[:idx] + '1' + trinarys[idx + 1:], 3)
        if tmp1 in sub_set:
            answer = tmp1
            break
        elif tmp2 in sub_set:
            answer = tmp2
            break
    
    print(f'#{tc} {answer}')