#use of hash function
hash_string = hash("Python")
hash_num = hash(42)
hash_tup = hash((1,2,3))

print(f"Hash of string: {hash_string}")
print(f"Hash of number: {hash_num}")
print(f"Hash of tuple: {hash_tup}")

print("\n")

#use of hashtable
hash_table = {}
hash_table["name"] = "Niharika"
hash_table["age"] = 19
hash_table["city"] = "New york"
hash_table["cou"] = "B.TECH CSE"

print(f"Name: {hash_table['name']}")
print(f"Age: {hash_table['age']}")
print(f"City: {hash_table['city']}")
print(f"Course: {hash_table['cou']}")