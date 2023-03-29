
# Pythono3 code to rename multiple
# files in a directory or folder

# importing os module
import os
# Function to rename multiple files
def main():

    for count, filename in enumerate(os.listdir("manifest2021")):
        src = 'manifest2021/' + filename
        srcext = os.path.splitext(filename)[1]
        dst = 'Reward' + str(count) + srcext
        dst = 'manifest2021/' + dst
        # rename() function will
        # rename all the files
        os.rename(src, dst)

# Driver Code
if __name__ == '__main__':

    # Calling main() function
    main()
