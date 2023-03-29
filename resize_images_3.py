#!/usr/bin/python
from PIL import Image
import os, sys

#path is the direcory
path = "/home/ict/Documents/Code/websites_etc/Websites/onlineivan/assets/img/2021Jul/"
#a list of files in the path
dirs = os.listdir( path )

def resize():
    #the item object is an obj of the filename with extension(basically each item of the dirs list)
    for item in dirs:
        # isfile takes two peramteres:
        # path - a string or bytes object representing a path
        # (Return Type) - boolean, returns true if file is existing
        f, e = os.path.splitext(path+item)
        if os.path.isfile(path+item):
            with Image.open(path+item) as im:
                print(str(im))
                new = im.thumbnail((720,720))
                #new = new.convert('RGB')
            #print(f'{imResize}')
            #Convert and save
            # use this for when using "resize" above - ###.convert('RGB')###
            #print(str(imResize))
            #os.remove(item)
            try:
                print(str(new))
                #new.Image.fromarray(new, "RGB").save(f + '.jpg' )
                new.save(path + item + e, "JPEG")  ###,'JPEG', quality=90###
            except AttributeError:
                print("Not working yet.. {}".format(new))

def delete():
    os.remove(item)

resize()
#delete()
