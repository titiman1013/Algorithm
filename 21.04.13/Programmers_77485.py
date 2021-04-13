def create_arr(rows, columns):
    num = 0
    arr = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            num += 1
            arr[i][j] = num
    return arr

    # return  board = [[i+(j)*columns for i in range(1,columns+1)] for j in range(rows)]


def rotate(arr, x1, x2, y1, y2):
    num_lst = [arr[x1 - 1][y1 - 1]]
    for i in range(y1, y2):
        num_lst.append(arr[x1 - 1][i])
        arr[x1 - 1][i] = num_lst[-2]
    for i in range(x1, x2):
        num_lst.append(arr[i][y2 - 1])
        arr[i][y2 - 1] = num_lst[-2]
    for i in range(y2 - 2, y1 - 2, -1):
        num_lst.append(arr[x2 - 1][i])
        arr[x2 - 1][i] = num_lst[-2]
    for i in range(x2 - 2, x1 - 2, -1):
        num_lst.append(arr[i][y1 - 1])
        arr[i][y1 - 1] = num_lst[-2]
    return arr, min(num_lst)

def solution(rows, columns, queries):
    answer = []

    arr = create_arr(rows, columns)

    for querie in queries:
        x1, y1, x2, y2 = querie
        arr, min_num = rotate(arr, x1, x2, y1, y2)
        answer.append(min_num)

    return answer




print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution(100, 97, [[1,1,100,97]]))

# answer 
# [8, 10, 25]
# [1, 1, 5, 3]
# [1]