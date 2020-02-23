T = int(input())
for n in range(T):
    numbers = [input() for i in range(5)]
    num_len = 0
    result = []
    for number in numbers:
        a = len(number)
        if num_len < len(number):
            num_len = len(number)
     
    for idx, i in enumerate(numbers):
        temp = num_len
        while temp - len(i) != 0:
            numbers[idx] += ' '
            temp -= 1
 
    for i in range(num_len):
        for j in range(len(numbers)):
            result.append(numbers[j][i])
 
    print(f'#{n+1}', end=' ')
    for i in result:
        if i == ' ':
            pass
        else:
            print(f'{i}', end='')
    print('')