
# Pythono3 code to rename multiple
# files in a directory or folder

# importing os module
import os
import datetime
import re
#puts me in the files directory
target = input('Enter full path: ')
prefix = input('Prefix:')
os.chdir(target)
allfiles = os.listdir(target)
#for each file in directory
for i in allfiles:
    #filename and extension = split extension (to keep the extension and work iwth name only)
    f_name, f_ext = os.path.splitext(i)
    #filters for characters to replace
    newer_name = f_name.replace("IMG", "")
    newer_name = newer_name.replace("img", "")
    newer_name = newer_name.replace("Zapper", "")
    newer_name = newer_name.replace("artflow", "")
    newer_name = newer_name.replace("-", "", 3)
    newer_name = newer_name.replace("(", "")
    newer_name = newer_name.replace(")", "")
    newer_name = newer_name.replace("_", "")
    newer_name = newer_name.replace(".", "", 2)
    newer_name = newer_name.replace("2021072", "")
    newer_name = newer_name.replace("58092021072111", "")

    newer_name = newer_name.replace("202108031602131115803111580311158031115803111", "")
    newer_name = newer_name.replace("414n19596576320", "")
    #re.sub(r'111[A-Za-z0-9]{3}', '', i)
    t = os.path.getctime(i)
    v = datetime.datetime.fromtimestamp(t)
    x = v.strftime('%Y%m%d%H%M%S')

    #print("Created")
    #print(os.stat(i)[-1])
    #print(os.stat(file).st_ctime)
    #print(os.path.getctime(file))


    '''
    #OTHER METHODS I experimented with:
    # .find('e.g.text')
    # .strip(etc)
    #f_title = f_name.strip(f_junk)
    #cutoff, leftover = f_name.split('-') - works with splitable delimeter type scenario
    '''

    new_name = f"{newer_name}{f_ext}"
    #os.rename(x + f_name, prefix + f_ext)
    os.rename(i, x + new_name)


#would like to add here a loop that checks if the string is longer than 5 characters
#if it is longer than 5 then delete characters 6 till infinity

#Then I want to prepend the file name with the filenames creation date


'''
# Function to rename multiple files
def main():
    for i in os.listdir( path ):
        #os.rename(path + i, path + i[4:8] + ".JPG")
        os.rename(path + i, path + "New" + i )

    for count, filename in enumerate(directory):
        new_name = "New" + str(count) + filename
        #new_path = "/" + path + "/" + new_name
        print(filename)
        #new_name = add + keep + str(count) + suff
        #src ='xyz'+ filename
        #dst ='xyz'+ dst

        # rename() function will
        # rename all the files
        os.rename(filename, new_name)

# Driver Code
if __name__ == '__main__':

    # Calling main() function
    main()
'''
