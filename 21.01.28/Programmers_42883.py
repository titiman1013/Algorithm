def solution(number, k):
    answer = ''

    num_lst = list(map(int, number))
    temp = num_lst[0]
    idx = 0
    for i, val in enumerate(num_lst[1:k]):
        if val > temp:
            idx = i + 1
            temp = val
            break
    k_temp = k
    if idx:
        k_temp -= idx
    
    while k_temp:
        pass    
    

    return answer





print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))