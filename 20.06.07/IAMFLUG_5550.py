import sys; sys.stdin = open('IAMFLUG.txt', 'r')

for tc in range(1, int(input())+1):
    arr = input()

    waiting = 0
    stop_machine = 0
    res = 0
    # sound = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
    sound = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    for i in range(len(arr)):
        if stop_machine:
            break

        if arr[i] == 'c':
            if waiting:
                # sound['c'] += 1
                sound[0] += 1
                waiting -= 1
            else:
                res += 1
                # sound['c'] += 1
                sound[0] += 1
        elif arr[i] == 'k':
            temp = 0
            for j in range(len(sound)-1):
                if sound[j]:
                    temp += 1
                else:
                    stop_machine += 1
                    res = -1
                    break
            if temp == 5:
                for k in range(len(sound)):
                    sound[k] -= 1
                waiting += 1
        else:
            # sound[arr[i]] += 1
            if arr[i] == 'r':
                sound[1] += 1
            elif arr[i] == 'o':
                sound[2] += 1
            elif arr[i] == 'a':
                sound[3] += 1

    print(f'#{tc} {res}')
