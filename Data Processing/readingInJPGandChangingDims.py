import os
import shutil
from PIL import Image
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

#path =r"C:\Users\const\Desktop\ADNI_Annual_2Yr_3T"
Oasispath = r'C:\Users\const\Desktop\newOasisJPGS'
ADNIpath = r'C:\Users\const\Desktop\adniBaseline'
pathToSave = r'C:\Users\const\Desktop\allBaselineImages'
minW = 10000
minH = 10000
start = True
for root, dirs, files in os.walk(Oasispath):
    for file in files:
        ending = file[-4:]
        if ending == ".jpg":
            if start:
                #print(file)
                #WANT: 160x208
                fullName = os.path.join(root,file)
                print(fullName)

                im = Image.open(fullName)
                print(im.size)
                newIm = im.resize((160,208))

                newImPath = os.path.join(pathToSave,file)
                newIm.save(newImPath)
                #w,h = im.size
                
                #if w < minW:
                #    minW = w
                #if h < minH:
                #    minH = h
                #if w != 176 or h != 208:
                #    print("WE GOT A PROBLEM")
                #start = False
                

            
                
            #print("---------")

for root, dirs, files in os.walk(ADNIpath):
    for file in files:
        ending = file[-4:]
        if ending == ".jpg":
            if start:
                #print(file)
                #WANT: 160x208
                fullName = os.path.join(root,file)
                print(fullName)

                im = Image.open(fullName)
                print(im.size)
                newIm = im.resize((160,208))

                newImPath = os.path.join(pathToSave,file)
                newIm.save(newImPath)
#print("minw: ", minW)   
#print("minh: ", minH)        



