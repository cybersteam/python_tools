import os


Path = input("Type in the full path of the directory you want to count files in: ")
#os.walk returns a generator , that creates a tuple of values
#(current_path, directories in current_path, files in current_path)
fileCount = sum(len(files) for _, _, files in os.walk(Path))
dirCount = sum(len(dirs) for _, dirs, _ in os.walk(Path))

#I still dont understand the first argument of os.walk - what is it exactly?
#hereCount = sum(len(root) for root, _, _ in os.walk(Path))
#print ("number of roots : ", hereCount)


print ("number of files : ", fileCount)
print ("number of dirs : ", dirCount)
