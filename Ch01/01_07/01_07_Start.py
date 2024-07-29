# Least to Greatest
myNums = [20, -10, 35, 11, 6, 2]
print(sorted(myNums))

# Alphabetically
print(sorted(['Bob', "Jack", 'Alice']))
print(sorted(['Jack', "Bob", 'alice']))

# Key Parameters
print(sorted('Jack bob alice Cathy'.split(), key=str.lower))

print(sorted([('Bob', 'C', 15), ('Jake', 'A', 14), ('Alice', 'B', 16)], key = lambda x : x[1]))