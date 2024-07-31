# Random Module
import random

# Random Numbers
print(random.random())

coinToss = random.randrange(2)
print('Heads') if coinToss == 0 else print('Tails')
print(coinToss)

diceRoll = random.randrange(1, 7)
print('You rolled a ' + str(diceRoll))

# Random Choices
winners = random.sample(range(100), 5)
print(winners)

whatToEat = random.choice(['Pasta', 'Burger', 'Lasagnia', 'Pizza', 'Cake'])
print(whatToEat)

cards = ['A', 'K', 'Q', 'J', '10', '9', 8, 7]
random.shuffle(cards)
print(cards)
