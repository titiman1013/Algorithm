def manu(name, go, min_cnt):
    idx = 0
    res = ['A'] * len(name)
    while name != res:
        if ord(name[idx]) - 65 > 13:
            min_cnt += 91 - ord(name[idx])
        else:
            min_cnt += ord(name[idx]) - 65
        res[idx] = name[idx]
        idx += go
        if name == res: break
        else:
            min_cnt += 1
    return min_cnt


def solution(name):
    answer = 0

    # A는 65
    # 문자를 숫자로 => ord
    # 숫자를 문자로 => char

    # print(ord('A'))
    # print(ord('Z'))

    # cnt_lst = [0] * len(name)
    # for i in range(len(name)):
    #     if ord(name[i]) - 65 > 13:
    #         cnt_lst[i] = 91 - ord(name[i])
    #     else:
    #         cnt_lst[i] = ord(name[i]) - 65

    name_lst = list(map(str, name))
    answer += min(manu(name_lst, 1, 0), manu(name_lst, -1, 0))

    return answer




print(solution("JEROEN"))
print(solution("JAN"))
print(solution("JAZ"))
print(solution("BBBAAAB"))
print(solution("ABABAAAAABA"))

# answer
# 56
# 23
# 11
# 9
# 11