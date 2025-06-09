#To print even numbers from 0 to 20
print("Even numbers from 0 to 20: ")
for i in range(0,21,1):
    if(i % 2 == 0):
        print(i)
    
#Example:
for i in range(1,5):
    for j in range(1,5):
        print(f"{i} * {j} = {i*j}")