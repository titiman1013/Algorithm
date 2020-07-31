import sys; sys.stdin = open('under 1million decimal.txt', 'r')

for i in range(1, 1000000, 2):
    if i == 1:
        print(2, end=" ")
        continue
    
    str_val = str(i)
    temp = 0
    for j in range(len(str_val)):
        temp += int(str_val[j])
    if temp == 3:
        print(3, end=" ")
        continue
    if temp % 3:
        for j in range(2, i):
            if i != j and i % j == 0:
                break
        else:
            print(i, end=" ")