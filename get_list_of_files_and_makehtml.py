import os
import  time
#os.path,

path = '/home/ict/Documents/Code/websites_etc/Websites/onlineivan/assets/img/2021Aug_2'

html_output = ''


files = []
files = os.listdir(path)

#created = time.ctime(os.path.getctime(name))

for name in files:
	#print

    code = f"\n<a \n\ttitle = \"Temp\" \n\tclass = \"Gallery_Photo\" \n\tstyle = \"background-image: url(\'/assets/img/2021Aug_2/{name}\')\">\n</a>"
    html_output = code
    #html_output += ''
    print(html_output)

    #html_output += f'\n\t<li>{name}</li>'
    #for name in names:
    #print(name)


'''
names.append(f"{line[0]} {line[1]}") #can be dictionary keys if DictReader

html_output += f'<p>There are {len(names)} this that text.</p>'
'''
