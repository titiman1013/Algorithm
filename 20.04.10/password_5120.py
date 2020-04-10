import sys; sys.stdin = open("password.txt", "r")

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

    def specialAdd(self, index):
        cur_idx = 0
        cur_node = self.head
        first_node = cur_node.next
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                if index != self.size:
                    new_node = Node(last_node.data + cur_node.data)
                    last_node.next = new_node
                    new_node.next = cur_node
                    self.size += 1
                    return
                else:
                    new_node = Node(last_node.data + first_node.data)
                    last_node.next = new_node
                    self.size += 1
                    return
            cur_idx += 1


for tc in range(1, int(input())+1):
    my_list = LinkedList()
    N, M, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    for number in numbers:
        my_list.append(number)

    idx = 0
    for i in range(K):
        idx += M
        if idx > my_list.size:
            idx = idx % my_list.size
        my_list.specialAdd(idx)
    result = my_list.display()
    result.reverse()
    if len(result) > 10:
        result = result[:10]
    res = ' '.join(list(map(str, result)))
    
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
#         self.size = 0

# def addLast(lst, new):
#     if lst.head is None:
#         lst.head = new
#         new.prev = new.next = new
#     else:
#         tail = lst.head.prev
#         new.prev = tail
#         new.net = lst.head
#         tail.next = new
#         lst.head.prev = new

#     lst.size += 1

# def printList(lst):
#     if lst.head is None: return
#     cur = lst.head
#     for _ in range(lst.size):
#         print(cur.data, end=' ')
#         cur = cur.next
#     print()
#     cur = lst.head.prev
#     for _ in range(lst.size * 2):
#         print(cur.data, end= ' ')
#         cur = cur.prev
#     print()

# for tc in range(1, int(input())+1):
#     N, M, K = map(int, input().split())
#     mylist = LinkedList()
#     arr = list(map(int, input().split()))
#     for val in arr:
#         addLast(mylist, Node(val))
#     cur = mylist.head
#     for _ in range(M):
#         for _ in range(K):
#             cur = cur.next
        
#         prev = cur.prev
#         new = Node(prev.data + cur.data, prev, cur)
#         prev.next = new
#         cur.prev = new
#         cur = new   # 새로 추가된 위치를 시작위치로 재설정
#         mylist.size += 1
    
#     printList(mylist)




# #
# class Node:
#     def __init__(self, data, pre, link):    # 이중 연결리스트
#         self.data = data
#         self.pre = pre
#         self.link = link

# def addLast(data):
#     global pHead
#     if pHead is None:
#         t = Node(data, None, None)
#         pHead = pTail = t
#         pHead.pre = pHead.link = t
#         return

#     t = Node(data, pTail, pHead)
#     pHead.pre = pTail.link = t
#     pTail = t
#     return

# def insert(p):
#     b = p.pre
#     t = Node(b.data + p.data, b, p)
#     b.link = p.pre = t
#     return t

# def print_list():
#     p = pHead.pre
#     for _ in range(10):
#         print(p.data, end=' ')
#         if p == pHead:
#             break
#         p = p.pre



# for tc in range(1, int(input())):
#     N, M, K = map(int, input().split())
#     s = list(map(int, input().split()))
#     pHead = pTail = None

#     for data in s:
#         addLast(data)

#     p = pHead
#     print(f'#{tc}', end=' ')
#     for i in range(K):
#         for j in range(M):
#             p = p.link
#         p = insert(p)
#     print_list()
#     print()