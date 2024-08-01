# Zipfile Module
import zipfile

# Open and List
myZipFile = zipfile.ZipFile('Archive.zip', 'r')
print(myZipFile.namelist())

# Metadata in the zip folder
# print(myZipFile.infolist())
for item in myZipFile.infolist():
    print(item)

print(myZipFile.getinfo('purchased.txt'))

# Access to files in zip folder
print(myZipFile.read('purchased.txt'))

with myZipFile.open('wishlist.txt', 'r') as f:
    print(f.read())

# Extracting files
# myZipFile.extract('purchased.txt')
myZipFile.extractall()

# Closing the zip
myZipFile.close()
