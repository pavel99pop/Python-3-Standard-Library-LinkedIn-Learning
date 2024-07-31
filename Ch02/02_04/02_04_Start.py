# Statistics Module
import statistics
import math

myData = [5, 10, 22, 11, 5, 10, 4, 35, 10, 2, 11, 10, 35, 85, 65, 4, 25]

print(statistics.mean(myData))
print(statistics.median(myData))
print(statistics.mode(myData))

print(sorted(myData))

print(statistics.variance(myData))
print(statistics.stdev(myData))

print(math.sqrt(statistics.variance(myData)))