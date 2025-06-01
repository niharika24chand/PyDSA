import queue
#FIFO QUEUE:
fifo_que = queue.Queue()

#insertion
fifo_que.put('A')
fifo_que.put('B')
fifo_que.put('C')
fifo_que.put('D')

print(fifo_que.get())
print(fifo_que.get())
print(fifo_que.get())
print(fifo_que.get())

print("____________________")

#PRIORITY QUEUE:
priority_que = queue.PriorityQueue()

#insertion
priority_que.put((2, 'Low priority task'))
priority_que.put((0, 'High priority task'))
priority_que.put((3, 'Medium priority task'))
priority_que.put((1, 'Low priority task'))

print(priority_que.get())
print(priority_que.get())
print(priority_que.get())
print(priority_que.get())