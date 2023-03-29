#!/usr/bin/python
from PIL import Image
import os, sys

path = "/home/ict/Documents/Code/websites_etc/Websites/onlineivan/assets/img/2021Jul/"
dirs = os.listdir( path )

#Image.open('old.jpeg').convert('RGB').save('new.jpeg')

size = 720, 720

def resize():
    for item in dirs:
        # isfile takes two peramteres:
        # path - a string or bytes object representing a path
        # item - (Return Type) - boolean, returns true if file is existing
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)

            # runs a resize function on the current file
            # resize takes size and resample(an optional resampling filter())
            #but here we used thumbnail instead
            imResize = im.thumbnail(size)
            #Convert and save
            # use this for when using "resize" above - ###.convert('RGB')###

            #os.remove(item)
            try:
                #PIL.Image.fromarray(image, "RGB").save(f + '.jpg' )
                imResize.save(f + '.jpg' )  ###,'JPEG', quality=90###
            except AttributeError:
                print("Couldn't save image {}".format(imResize))

def delete():
    os.remove(item)

resize()
#delete()
