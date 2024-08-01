# Command Line Arguments
import sys

# Print Arguments
print(len(sys.argv))

# Remove Arguments
sys.argv.remove(sys.argv[0])
print(sys.argv)

# Sum up the Arguments
sum = 0
for item in sys.argv:
    try:
        sum += int(item)
    except Exception:
        print('Invalid input!')

print(sum)