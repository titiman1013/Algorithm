import heapq

def solution(operations):
    answer = []

    heap = []
    for operation in operations:
        command, num = operation.split()
        if command == 'I':
            heapq.heappush(heap, int(num))
        elif command == 'D':
            if heap:
                if num == '1':
                    reverse_heap = [-val for val in heap]
                    heapq.heapify(reverse_heap)
                    heapq.heappop(reverse_heap)
                    heap = [-val for val in reverse_heap]
                    heapq.heapify(heap)
                elif num == '-1':
                    heapq.heappop(heap)

    if heap:
        answer = [max(heap), min(heap)]
    else:
        answer = [0, 0]

    return answer




print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))

# answer
# [0, 0]
# [7, 5]