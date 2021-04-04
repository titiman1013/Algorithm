# clear

# def solution(n, words):
#     answer = []

#     used_words = set()
#     cur_word = ''
#     turns = [0] * n
#     for idx, word in enumerate(words):
#         if idx == 0:
#             turns[0] += 1
#             cur_word = word[-1]
#             used_words.add(word)
#         else:
#             turns[idx % n] += 1
#             if word[0] == cur_word and word not in used_words:
#                 cur_word = word[-1]
#                 used_words.add(word)
#             else:
#                 answer.append(idx % n + 1)
#                 answer.append(turns[idx % n])
#                 break
#     else:
#         answer = [0, 0]

#     return answer


#

def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p - 1][-1] or words[p] in words[:p]: return [(p % n) + 1, (p // n) + 1]
    else:
        return [0, 0]
        




print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))

# answer
# [3, 3]
# [0, 0]
# [1, 3]