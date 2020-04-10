import sys; sys.stdin = open("sequence combine.txt", "r")

# # 10개중 7개
# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     arr = []
#     for i in range(M):
#         temp = list(map(int, input().split()))
#         if len(arr) == 0:
#             for j in range(len(temp)):
#                 arr.append(temp[j])
#         else:
#             for j in range(len(arr)):
#                 if temp[0] < arr[j]:
#                     for k in range(len(temp)):
#                         arr.insert(j+k, temp[k])
#                     break
#                     # head = arr[:j]
#                     # tail = arr[j:]
#                     # for k in range(len(temp)):
#                     #     head.append(temp[k])
#                     # head += tail
#                     # arr = head
#             else:
#                 for k in range(len(temp)):
#                     arr.append(temp[k])

#     print(f'#{tc}', end=' ')
#     for i in range(len(arr)-1, len(arr)-11, -1):
#         print(arr[i], end=' ')
#     print()




# # 10개중 9개
# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     arr = []
#     for i in range(M):
#         if len(arr) != 0:
#             temp = list(map(int, input().split()))
#             for j in range(len(arr)):
#                 if arr[j] > temp[0]:
#                     tail = arr[j:]
#                     arr = arr[:j]
#                     for k in range(len(temp)):
#                         arr.append(temp[k])
#                     arr += tail
#                     # print(arr)
#                     # print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
#                     break
#             else:
#                 arr += temp
#                 # print(arr)
#                 # print('mmmmmmmmmmmmmmmm')
#         else:
#             arr = list(map(int, input().split()))
#         # arr = arr[len(arr)-1:len(arr)-11]
#     # print(arr)
#     # print('ㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣ')
#     print(f'#{tc}', end=' ')
#     for i in range(len(arr)-1, len(arr)-11, -1):
#         print(arr[i], end=' ')
#     # arr.reverse()
#     # for i in range(10):
#     #     print(arr[i], end=' ')
#     print()



#
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node
        self.size += 1

    def display(self):
        elems = []
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            elems.append(cur.data)
        return elems

    def add(self, index, data):
        new_node = Node(data)
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = new_node
                new_node.next = cur_node
                self.size += 1
                return
            cur_idx += 1

    def merge(self, numbers):
        cur_node = self.head
        cur_idx = 0
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == self.size or cur_node.data > numbers[0]:
                for number in numbers[::-1]:
                    my_list.add(cur_idx, number)
                return
            cur_idx += 1


for tc in range(1, int(input())+1):
    my_list = LinkedList()
    N, M = map(int, input().split())

    for i in range(M):
        numbers = list(map(int, input().split()))
        if i == 0:
            for number in numbers:
                my_list.append(number)
        else:
            my_list.merge(numbers)

    result = my_list.display()
    result.reverse()
    res = ' '.join(list(map(str, result[:10])))
    
    print(f'#{tc} {res}')





# #
# class Node:
#     def __init__(self, d=0, p=None, n=None):
#         self.data = d
#         self.prev = p
#         self.next = n

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0

# # def addList(lst, new):
# #     if lst.head is None:
# #         lst.head = lst.tail = new
# #     else:
# #         new.prev = lst.tail
# #         lst.tail.next = new
# #         lst.tail = new
# #     lst.size += 1

# def addList(lst, arr):
#     first = last = Node(arr[0])
#     for val in arr[1:]:
#         new = Node(val, last)
#         last.next = new
#         last = new
    
#     # 빈리스트일때
#     if lst.head is None:
#         lst.head, lst.tail = first, last
#     else:
#         cur = lst.head
#         while cur is not None:
#             if cur.data > arr[0]: break
#             cur = cur.next
#         if cur is None: # 뒤에 추가하는 것
#             first.prev = lst.tail
#             lst.tail.next = first
#             lst.tail = last
#         elif cur.prev is None:  # 앞에 추가하는 것
#             last.next = lst.head
#             lst.head.prev = last
#             lst.head = first
#         else:   # 중간에 추가하는 것
#             prev = cur.prev
#             first.prev= prev # == cur.prev
#             last.next = cur
#             prev.next = first
#             cur.prev = last
#     lst.size += len(arr)

# def printList(lst):
#     if lst.head is None: return
#     cur = lst.head
#     while cur is not None:
#         print(cur.data, end=' ')
#         cur = cur.next
#     print()
#     cur = lst.tail
#     while cur is not None:
#         print(cur.data, end=' ')
#         cur = cur.prev
#     print()

# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     mylist = LinkedList()
#     for i in range(M):
#         arr = list(map(int, input().split()))
#         addList(mylist, arr)
#     printList(mylist)