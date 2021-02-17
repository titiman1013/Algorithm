def transform_binary(n, arr):
    bin = []
    for val in arr:
        temp = str(format(val, 'b'))
        if len(temp) < n:
            temp = '0' * (n - len(temp)) + temp
        bin.append(temp)
    return bin


def solution(n, arr1, arr2):
    answer = []

    temp_map1 = transform_binary(n, arr1)
    temp_map2 = transform_binary(n, arr2)
    
    for i in range(n):
        string = ''
        for j in range(n):
            if temp_map1[i][j] == '1' or temp_map2[i][j] == '1':
                string += '#'
            else:
                string += ' '
        answer.append(string)

    return answer




print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))

# answer
# ["#####","# # #", "### #", "# ##", "#####"]
# ["######", "### #", "## ##", " #### ", " #####", "### # "]