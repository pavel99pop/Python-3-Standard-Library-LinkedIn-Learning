# Range -> range instance that holds all nums counting by one between 0 and first input
# List -> lists numbers from the inputted tuple

players = range(30)
print(list(players))

for player in players:
    print('Player #' + str(player) + ' just joined')

losers = range(7, 30, 5)
print(f'The losers are: {list(losers)}')