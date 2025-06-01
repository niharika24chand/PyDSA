#implementing queue using list
import queue
queue_list = []

queue_list.append('G')
queue_list.append('O')
queue_list.append('W')
queue_list.append('S')
queue_list.append('T')

print("Queue before: ", queue_list)

queue_list.pop(0)
queue_list.pop(0)

print("Queue after: ", queue_list)