#caching with a dict like a hashtable

cache ={}
def expensive_computation(i):
    if i in cache:
        print(f"Fetching result for {i} from cache")
        return cache[i]
    else:
        print(f"Computing result for {i}: ")
        result = i * i
        return result


print(expensive_computation(5))
print(expensive_computation(10))
print(expensive_computation(5))
print(expensive_computation(6))

print("\n")

#indexing with a dict like a hashtable
student_scores ={
    "Naina" : 80,
    "Arjun" : 88,
    "Hardik" : 56,
    "Kanishka" : 91
}

for student in student_scores:
    print(f"{student}: {student_scores[student]}")