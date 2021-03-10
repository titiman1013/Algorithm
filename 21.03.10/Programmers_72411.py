from itertools import combinations

def check(orders, cnt, menu_dic):
    for order in orders:
        order = sorted(list(map(str, order)))
        lst = list(combinations(order, cnt))
        for val in lst:
            tmp = "".join(val)
            if menu_dic.get(tmp):
                menu_dic[tmp] += 1
            else:
                menu_dic[tmp] = 1
    return menu_dic


def solution(orders, course):
    answer = []

    for cnt in course:
        menu_dic = {}
        menu_dic = check(orders, cnt, menu_dic)

        maxi = 0
        menu = []
        for key, val in menu_dic.items():
            if val > 1:
                if val > maxi:
                    maxi = val
                    menu = [key]
                elif val == maxi:
                    menu.append(key)
        if menu:
            answer += menu
    
    answer.sort()

    return answer




print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))

# answer
# ["AC", "ACDE", "BCFG", "CDE"]
# ["ACD", "AD", "ADE", "CD", "XYZ"]
# ["WX", "XY"]