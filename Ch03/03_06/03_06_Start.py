# Tempfile Module
import tempfile

# Create a temporary file
myTempFile = tempfile.TemporaryFile()

# Write to a temporary file
myTempFile.write(b'Yo here goes my digits: 69420')
myTempFile.seek(0)

# Read the temporary file
print(myTempFile.read())

# Close the temporary file
myTempFile.close()