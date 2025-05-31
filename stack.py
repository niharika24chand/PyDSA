#Implementing stack using a list
stack = []

#push operation
stack.append(20)
stack.append(40)
stack.append(60)
stack.append(80)

print("Stack after pushes: ",stack)

#pop operation
popped_element = stack.pop()
print("Popped element: ",popped_element)
print("Stack after pop: ",stack)

#peek operation
top_element=stack[-1]
print("Peek element: ",top_element)
print("Stack after peek: ",stack)

#To check whether stack is empty using length
stack1 = [23,45,67,89]
def is_empty(stack1):   
    return len(stack1) == 0
while not is_empty(stack1):
    stack1.pop()
    print("Current stack: ",stack1)

print("Is the stack empty? ",is_empty(stack1))

