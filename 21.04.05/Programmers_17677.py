from collections import Counter

def cluster_str(strings):
    cluster = []
    L = len(strings)
    for idx, string in enumerate(strings):
        if idx == L - 1:
            break
        else:
            if string.isalpha() and strings[idx + 1].isalpha():
                cluster.append(strings[idx:idx+2].upper())
    return cluster


def solution(str1, str2):
    answer = 0

    multi_a, multi_b = cluster_str(str1), cluster_str(str2)
    counter_a, counter_b = Counter(multi_a), Counter(multi_b)
    union = set(multi_a) | set(multi_b)
    intersection = set(multi_a) & set(multi_b)
    
    union_cnt = 0
    for union_val in union:
        union_cnt += max(counter_a[union_val], counter_b[union_val])
    inter_cnt = 0
    for inter_val in intersection:
        inter_cnt += min(counter_a.get(inter_val), counter_b.get(inter_val))
    
    if union_cnt == 0 and inter_cnt == 0:
        answer = 1 * 65536
    else:
        answer = int(inter_cnt / union_cnt * 65536)

    return answer




print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))

# answer
# 16384
# 65536
# 43690
# 65536