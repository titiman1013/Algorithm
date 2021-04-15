# false

# from itertools import combinations
# from collections import Counter

# def solution(relation):
#     answer = 0

#     N, M = len(relation), len(relation[0])

#     attributes = [i for i in range(M)]
#     for m in range(1, M + 1):
#         clusters = list(combinations(attributes, m))
#         for cluster in clusters:
#             check_lst = set()
#             for num in cluster:
#                 tmp_lst = set()
#                 for i in range(N):
#                     tmp_lst.add(relation[i][num])
#                 check_lst.add(tmp_lst)
            
#     return answer


#

from itertools import chain, combinations

def create_comb(iterable):
    tmp_lst = list(iterable)
    return chain.from_iterable(combinations(tmp_lst, r) for r in range(1, len(tmp_lst) + 1))


def solution(relation):
    answer = 0

    N, M = len(relation), len(relation[0])
    
    clusters1 = []
    for combi in create_comb(range(M)):
        check_set = set()
        for i in range(N):
            check_set.add(tuple(relation[i][j] for j in combi))
        if len(check_set) == N:
            clusters1.append(combi)

    clusters2 = []
    for i in range(len(clusters1) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if set(clusters1[i]) & set(clusters1[j]) == set(clusters1[j]):
                clusters2.append(clusters1[i])
                break

    answer = len(clusters1) - len(clusters2)

    return answer





print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))

# answer
# 2