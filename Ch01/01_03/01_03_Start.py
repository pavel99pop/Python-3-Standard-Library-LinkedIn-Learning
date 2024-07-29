# Calculating Length

# len() --> returns length
firstName = 'Alexi'
print(len(firstName))
lastName = 'Laiho'
print(lastName.__len__())

ages = [1, 50, 16, 28, 21, 30]
print(len(ages))

for i in range(0, len(ages)):
    print(ages[i])

print(len(['bob', 'john', 'alice']))

albumCollection = {'bob': 5, 'john': 12, 'alice': 2}
print(len(albumCollection))