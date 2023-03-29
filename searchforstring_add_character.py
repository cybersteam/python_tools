char1 = "-"
char2 = ","

def findChar(char1):
 return char1

def addChar(char2):
 return char2

#open the file
f = open("list.txt","r")
#read lines

lines = f.readlines()

f.close()
#NOW IT HAS IT IN MEMORY

f = open("new.txt","w")
for line in lines:
    if line.find(char1) == True:
        addChar()
        f.write(line)
f.close()

#if we find -
#add , before it

'''
s = 'python is fun'
c = 'n'
print(s.find(c))
'''
