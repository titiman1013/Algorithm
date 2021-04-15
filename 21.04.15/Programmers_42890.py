# false

from itertools import combinations
from collections import Counter

def solution(relation):
    answer = 0

    N, M = len(relation), len(relation[0])

    attributes = [i for i in range(M)]
    for m in range(1, M + 1):
        clusters = list(combinations(attributes, m))
        for cluster in clusters:
            check_lst = set()
            for num in cluster:
                tmp_lst = set()
                for i in range(N):
                    tmp_lst.add(relation[i][num])
                check_lst.add(tmp_lst)
            
    return answer
    




print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))

# answer
# 2