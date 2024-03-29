from collections import defaultdict


def solution(enroll, referral, seller, amount):
    answer = []

    in_recommends = defaultdict(str)
    for i in range(len(enroll)):
        if referral[i] != '-':
            in_recommends[enroll[i]] = referral[i]

    print(in_recommends)

    return answer




print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))
print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["sam", "emily", "jaimie", "edward"], [2, 3, 5, 4]))

# answer
# [360, 958, 108, 0, 450, 18, 180, 1080]
# [0, 110, 378, 180, 270, 450, 0, 0]