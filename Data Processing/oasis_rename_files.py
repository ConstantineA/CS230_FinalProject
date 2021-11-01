import os
import shutil

path =r"D:\CS 230\OASIS\oasis_images"

for count, filename in enumerate(os.listdir(path)):
        dst = filename[:13]
        src = path + "\\" + filename
        dst = path + "\\" + dst + ".gif"

        print(src, dst)
          
        # rename() function will
        # rename all the files
        os.rename(src, dst)