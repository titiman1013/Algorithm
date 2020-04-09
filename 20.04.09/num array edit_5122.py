import sys; sys.stdin = open("num array edit.txt", "r")

# for tc in range(1, int(input())+1):
#     N, M, L = map(int, input().split())
#     arr = list(map(int, input().split()))
#     edit_number = []
#     for i in range(M):
#         edit_number.append(list(input().split()))
    
#     # arr_list = []
#     # for i in range(len(arr)):
#     #     if i != len(arr) - 1:
#     #         arr_list.append([arr[i], arr[i+1]])
#     #     else:
#     #         arr_list.append([arr[i], 'None'])

#     for i in edit_number:
#         if i[0] == 'I':
#             arr.insert(int(i[1]), int(i[2]))
#         elif i[0] == 'D':
#             # arr.remove(arr[int(i[1])])
#             del arr[int(i[1])]
#         elif i[0] == 'C':
#             arr[int(i[1])] = int(i[2])

#     if L > len(arr) - 1:
#         print(f'#{tc} {-1}')
#     else:
#         print(f'#{tc} {arr[L]}')

#
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    # node의 다음값을 저장
    def add(self, node):
        if self.next in None:
            self.next = node
        else:
            n = self.next
            while True:
                if n.next in None:
                    n.next = node
                    break
                else:
                    n = n.next
    
    def select(self, idx):
        n = self.next
        for i in range(idx - 1):
            n = n.next
        return n.data

    def delete(self, idx):
        n = self.next
        for i in range(idx - 2):
            n = n.next
        t = n.next
        n.next = t.next
        del t

    # select와 delete함수를 합친 역할
    def pop(self, idx):
        n = self.next
        for i in range(idx - 2):
            n = n.next
        t = n.next
        n.next = t.next
        return t
    
    def insert(self, idx, node):
        n = self.next
        for i in range(idx - 2):
            n = n.next
        t = n.next
        n.next = node
        node.next = t

    # 전체노드를 출력
    def prt(self):
        n = self.next
        while True:
            if n.next is None:
                print(n.data, end=' ')
                break
            else:
                print(n.data, end=' ')
                n = n.next
        print()


# for tc in range(1, int(input())+1):
#     N, M, L = map(int, input().split())
