#implementing queue using deque
import queue
from collections import deque

queue_deq = deque()

queue_deq.append('H')
queue_deq.append('I')
queue_deq.append('M')
queue_deq.append('N')
queue_deq.append('P')

print("Queue before: ", queue_deq)

queue_deq.popleft()
queue_deq.popleft()
queue_deq.popleft()

print("Queue after: ", queue_deq)