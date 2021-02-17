#

# def transform_binary(n, arr):
#     bin = []
#     for val in arr:
#         temp = str(format(val, 'b'))
#         if len(temp) < n:
#             temp = '0' * (n - len(temp)) + temp
#         bin.append(temp)
#     return bin


# def solution(n, arr1, arr2):
#     answer = []

#     temp_map1 = transform_binary(n, arr1)
#     temp_map2 = transform_binary(n, arr2)
    
#     for i in range(n):
#         string = ''
#         for j in range(n):
#             if temp_map1[i][j] == '1' or temp_map2[i][j] == '1':
#                 string += '#'
#             else:
#                 string += ' '
#         answer.append(string)

#     return answer


#

def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        # i와 j를 이진수로 변환 후 같은 index중에 하나라도 1의 값을 가지면 1
        # 2부터 slicing한 이유는 앞에 0b가 붙기 때문
        temp = str(bin(i|j)[2:])
        temp = temp.rjust(n, '0')
        temp = temp.replace('1', '#')
        temp = temp.replace('0', ' ')
        answer.append(temp)
    return answer





print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))

# answer
# ["#####","# # #", "### #", "# ##", "#####"]
# ["######", "### #", "## ##", " #### ", " #####", "### # "]