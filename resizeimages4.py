#!/usr/bin/python
from PIL import Image
import os, sys

#This works but there is still work to do.. last time
#there were path problems, it only works from a current directory for now
#I want a cleaner way to deal with the path object
#as well as adding support for multiple file types
#
path = '/home/ict/Documents/Code/websites_etc/Websites/onlineivan/assets/img/2021Aug_2/'

#file = "/home/ict/Documents/Code/websites_etc/Websites/onlineivan/assets/img/2021Jul/1042.JPG"
#my_path = "/home/ict/Desktop/2021Jul"
os.chdir(path)
size_720 = (720,720)
file_list = os.listdir('.')

#current directoery
for file in file_list:
        file_obj = Image.open(file)
        #print(path + file)
        i = Image.open(file)
        fn, fext = os.path.splitext(file)

        i.thumbnail(size_720)
        #720e.g. is a new folder if you want in your path (you must create it first, this just references it)
        i.save(f'2021_{fn}{fext}')



'''
#current directoery
#for f in os.listdir('.'):
for f in os.listdir(path):
    if f.endswith('.JPG'):
        print(f)
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.thumbnail(size_720)
        #720e.g. is a new folder if you want in your path (you must create it first, this just references it)
        i.save(f'smalls/{fn}{fext}')

'''







#image = Image.open('1042.JPG')
#image.save('1042.png')
