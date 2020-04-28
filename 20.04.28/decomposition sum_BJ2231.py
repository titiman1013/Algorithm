N = int(input())

res = 1000001
for i in range(N):
    temp = i
    # print(temp)
    for j in range(len(str(i))):
        temp += int(str(i)[j])
    # print(temp)
    if temp == N:
        if temp < res:
            res = i

if res == 1000001:
    print(0)
else:
    print(res)

# 입력 216
# 출력 198