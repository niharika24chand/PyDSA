import heapq

heap = []
num = [2,9,1,4,7]
for i in num:
    heapq.heappush(heap, i)
s = heapq.heappop(heap)  #It removes and returns the smallest element from the heap while maintaining the heap property

print(f"Min-Heap: {heap}")
print(f"Smallest number: {s}")