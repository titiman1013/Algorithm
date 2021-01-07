def solution(phone_book):
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if i != j and len(phone_book[i]) <= len(phone_book[j]):
                cnt = 0
                for p in range(len(phone_book[i])):
                    if phone_book[i][p] == phone_book[j][p]:
                        cnt += 1
                if cnt == len(phone_book[i]):
                    return False
    
    return True
    
    
    # answer = True
    # return answer




print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))

# answer
# false
# true
# false