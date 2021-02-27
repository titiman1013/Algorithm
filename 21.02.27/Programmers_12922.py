def solution(n):
    answer = ''

    for i in range(1, n+1):
        if i % 2:
            answer += "수"
        else:
            answer += "박"

    return answer
    
    return "수박" * (n//2) + "수" * (n%2)




print(solution(3))
print(solution(4))

# answer
# 수박수
# 수박수박