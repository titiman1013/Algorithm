# from collections import Counter

# def cluster_str(strings):
#     cluster = []
#     L = len(strings)
#     for idx, string in enumerate(strings):
#         if idx == L - 1:
#             break
#         else:
#             if string.isalpha() and strings[idx + 1].isalpha():
#                 cluster.append(strings[idx:idx+2].upper())
#     return cluster


# def solution(str1, str2):
#     answer = 0

#     multi_a, multi_b = cluster_str(str1), cluster_str(str2)
#     counter_a, counter_b = Counter(multi_a), Counter(multi_b)
#     union = set(multi_a) | set(multi_b)
#     intersection = set(multi_a) & set(multi_b)
    
#     union_cnt = 0
#     for union_val in union:
#         union_cnt += max(counter_a[union_val], counter_b[union_val])
#     inter_cnt = 0
#     for inter_val in intersection:
#         inter_cnt += min(counter_a.get(inter_val), counter_b.get(inter_val))
    
#     if union_cnt == 0 and inter_cnt == 0:
#         answer = 1 * 65536
#     else:
#         answer = int(inter_cnt / union_cnt * 65536)

#     return answer


#

def solution(str1, str2):

    list1 = [str1[n:n+2].lower() for n in range(len(str1)-1) if str1[n:n+2].isalpha()]
    list2 = [str2[n:n+2].lower() for n in range(len(str2)-1) if str2[n:n+2].isalpha()]

    tlist = set(list1) | set(list2)
    res1 = [] # 합집합
    res2 = [] # 교집합

    if tlist:
        for i in tlist:
            res1.extend([i]*max(list1.count(i), list2.count(i)))
            res2.extend([i]*min(list1.count(i), list2.count(i)))

        answer = int(len(res2)/len(res1)*65536)
        return answer

    else:
        return 65536




print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))

# answer
# 16384
# 65536
# 43690
# 65536