# Itertools Part 2
import itertools

# Permutations: Order matters - some copies with same inputs but in different order
myTasks = ['Eat', 'Sleep', 'Play']
for i in itertools.permutations(myTasks):
    print(i)

# Combinations: Order does not matter - no copies with same inputs
comboMeals = ['Pizza', 'Sandwich', 'Fries', 'Pie', 'Salad']
for i in itertools.combinations(comboMeals, 2):
    print(i)