import os
import shutil
from PIL import Image
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

#path =r"C:\Users\const\Desktop\ADNI_Annual_2Yr_3T"
#Oasispath = r'C:\Users\const\Desktop\newOasisJPGS'
#ADNIpath = r'C:\Users\const\Desktop\adniBaseline'
path = r'C:\Users\const\Desktop\allBaselineImages'

start = True
for root, dirs, files in os.walk(path):
    for file in files:
        ending = file[-4:]
        if ending == ".jpg":
            if start:
                #print(file)
                #WANT: 160x208
                fullName = os.path.join(root,file)
                #print(fullName)

                im = Image.open(fullName)
                #print(im.size)
                if im.size != (160,208):
                    print("WE GOT A PROBLEM")



