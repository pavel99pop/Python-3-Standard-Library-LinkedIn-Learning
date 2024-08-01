# Files and File Writing

# Open a file
myFile = open('scores.txt', 'w')

# w --> write
# r --> read
# r+ --> read and write
# a --> append
# Show attributes and properties of that file
print(myFile.name)
print(myFile.mode)

# Write to a file
myFile.write('HBK : 69\nHHH : 42\nRVD : 71')
myFile.close()

# Read the file
myFile = open('scores.txt', 'r')
print(myFile.read(9))
print(myFile.read(9))
