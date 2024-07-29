print(type(5))
print(type('hello world'))

class Car:
    pass

class Truck(Car):
    pass

c = Car()
t = Truck()

print(type(c) == type(t))

print(isinstance(t, Car))

r = range(30)
if isinstance(r, range):
    print(list(r))