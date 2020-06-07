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
            if temp == 4:
                # print('check')
                for k in range(len(sound)-1):
                    sound[k] -= 1
                waiting += 1
        else:
            # sound[arr[i]] += 1
            if arr[i] == 'r':
                if sound[0]:
                    sound[1] += 1
                else:
                    stop_machine += 1
                    break
            elif arr[i] == 'o':
                if sound[0] and sound[1]:
                    sound[2] += 1
                else:
                    stop_machine += 1
                    break
            elif arr[i] == 'a':
                if sound[0] and sound[1] and sound[2]:
                    sound[3] += 1
                else:
                    stop_machine += 1
                    break
    
        # print(sound)

    for i in range(len(sound)):
        if sound[i]:
            res = -1
            break

    print(f'#{tc} {res}')