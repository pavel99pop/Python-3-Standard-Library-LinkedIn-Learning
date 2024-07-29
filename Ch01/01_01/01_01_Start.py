# Python Logical Operators: And, Or, Not:

# What is a Boolean?
isRaining = True
isSunny = False
# Logical Operators -> Special Operators for Booleans

# AND
# true and true --> true
# false and true --> false
# true and false --> false
# false and false --> false
if isRaining and isSunny:
    print('Rainbow!')

# OR
# true and true --> true
# false and true --> true
# true and false --> true
# false and false --> false
if isRaining or isSunny:
    print('I miss snow!')

# NOT
# true --> false
# false --> true
if not isSunny:
    print('Yay! no heat...')

ages = [15, 6, 12, 65, 28, 35, 22]
for age in ages:
    isAdult = age > 18
    if not isAdult:
        print('Age ' + str(age) + ' is not old enough!')