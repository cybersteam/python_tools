#!/usr/bin/python
from PIL import Image
import os, sys

#path is the direcory
path = "/home/ict/Documents/Code/websites_etc/Websites/onlineivan/assets/img/2021Jul/"
#a list of files in the path
dirs = os.listdir( path )

#Image.open('old.jpeg').convert('RGB').save('new.jpeg')

size = 720, 720

def resize():
    #the item object is an obj of the filename with extension(basically each item of the dirs list)
    for item in dirs:
        # isfile takes two peramteres:
        # path - a string or bytes object representing a path
        # (Return Type) - boolean, returns true if file is existing
        if os.path.isfile(path+item):
            #im is the entire image obj e.g <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=720x720 at 0x7FC4C75E2FD0>
            im = Image.open(path+item)
            #f is the path+filename
            #e is the extension needed for that file

            f, e = os.path.splitext(path+item)
            #print(f'path, item, f, e, dirs, size')

            # runs a resize function on the current file
            # resize takes size and resample(an optional resampling filter())
            #but here we used thumbnail instead
            imResize = im.thumbnail((720,720))
            #print(f'{imResize}')
            #Convert and save
            # use this for when using "resize" above - ###.convert('RGB')###
            #print(str(imResize))
            #os.remove(item)
            try:
                imResize.save(imResize)  ###,'JPEG', quality=90###
            except AttributeError:
                print("Couldn't save image {}".format(imResize))

def delete():
    os.remove(item)

resize()
#delete()
