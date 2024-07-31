# Itertools
import itertools

# Infinite Counting
for i in itertools.count(50, 10):
    print(i)
    if i == 80:
        break

# Infinite Cycling
x = 0
for i in itertools.cycle(['Apple', 'Banana', 'Cherry']):
    print(i)
    x += 1
    if x  == 10:
        break

# Infinite Repeating
for i in itertools.repeat('Play - Eat - Sleep'):
    print(i)
    x += 1
    if x == 20:
        break