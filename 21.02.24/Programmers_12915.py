def solution(strings, n):
    # answer = []

    # order_dict = {}
    # order_list = []
    # for idx, string in enumerate(strings):
    #     if order_dict.get(string[n]):
    #         order_dict[string[n]].append(idx)
    #     else:
    #         order_dict[string[n]] = [idx]
    #         order_list.append(string[n])
    
    # order_list.sort()
    # # print(order_list)

    # for string in order_list:
    #     vals = order_dict.get(string)
    #     if len(vals) > 1:
    #         temps = [(strings[val], val) for val in vals]
    #         temps.sort()
    #         vals = [temp[1] for temp in temps]
        
    #     for val in vals:
    #         answer.append(strings[val])

    # return answer

    return sorted(strings, key=lambda x: x[n])




print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))

# answer
# ["car", "bed", "sun"]
# ["abcd", "abce", "cdx"]