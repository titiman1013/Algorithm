import sys; sys.stdin = open('1232.txt', 'r')

def numeric_node(node_info, node_num):
    return int(node_info.get(node_num)[0])


def operator_node(node_info, node_num):
    operator, node1, node2 = node_info.get(node_num)
    node1, node2 = int(node1), int(node2)

    if len(node_info[node1]) != 1:
        node1 = operator_node(node_info, node1)
    else:
        node1 = numeric_node(node_info, node1)
    
    if len(node_info[node2]) != 1:
        node2 = operator_node(node_info, node2)
    else:
        node2 = numeric_node(node_info, node2)
    
    if operator == '+':
        return node1 + node2
    elif operator == '-':
        return node1 - node2
    elif operator == '*':
        return node1 * node2
    else:
        return node1 // node2



for tc in range(1, 11):
    N = int(input())
    node_info = dict()
    for _ in range(N):
        tmp_info = list(map(str, input().split()))
        node_info[int(tmp_info[0])] = tmp_info[1:]
    
    answer = operator_node(node_info, 1)
    print(f'#{tc} {answer}')