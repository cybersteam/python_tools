import os
from PIL import Image

# The directory that we are interested in
myPath = "."

# The min size of the file in Bytes
mySize = '50000'

# All the file paths will be stored in this list
filesList= []

for path, subdirs, files in os.walk(myPath):
    for name in files:
        filesList.append(os.path.join(path, name))

for i in filesList:
    # Getting the size in a variable
    fileSize = os.path.getsize(str(i))

    # Print the files that meet the condition
    if int(fileSize) >= int(mySize):
        print (f"The file:" + str(i) + " is: " + str(fileSize) + " Bytes")
