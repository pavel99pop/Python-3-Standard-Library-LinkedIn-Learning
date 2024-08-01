# Iterative Files
myFile = open("scores.txt", "r")

# Read one line at a time
print(myFile.readline())
myFile.seek(0)

# Iterate through each line of a file
for line in myFile:
    line = line.replace('KHD', 'HBK')
    print(line)

myFile.close()