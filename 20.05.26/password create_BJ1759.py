import sys; sys.stdin = open('password create.txt' ,'r')

def search(cnt, _sum, use):
    if cnt == L:
        consonant = 0
        vowel = 0
        for i in range(L):
            if _sum[i] == 'a' or _sum[i] == 'e' or _sum[i] == 'i' or _sum[i] == 'o' or _sum[i] == 'u':
                vowel += 1
            else:
                consonant += 1
        if vowel >= 1 and consonant >= 2:
            if _sum not in res_list:
                res_list.append(_sum)
        return


    for i in range(use+1, len(arr)):
        search(cnt+1, _sum+arr[i], i)



L, C = map(int, input().split())
arr = input().split()
arr.sort()

res_list = []
for i in range(len(arr)):
    search(1, arr[i], i)

for i in range(len(res_list)):
    print(res_list[i])