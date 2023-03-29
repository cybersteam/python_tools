phrase = str(raw_input("Enter a phrase:"))
f = open("old.txt","r")
lines = f.readlines()
f.close()
f = open("new.txt","w")
for line in lines:
    if phrase != line.strip():
        f.write(line)
f.close()
