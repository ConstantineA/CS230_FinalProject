import os
import shutil
from PIL import Image
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


rotatedFolder = r"C:\Users\const\Desktop\Data_Processing\ALL\rotated"
pathToSave = r'C:\Users\const\Desktop\Data_Processing\ALL\allComplete'
folderNames = ["1yr_1.5","1yr_3","2yr_1.5","2yr_3","3yr_1.5","3yr_3","base_2yr_3","base_3"]

start = True
for i in folderNames:
    folderPath = os.path.join(rotatedFolder,i)
    print(folderPath)
    for root, dirs, files in os.walk(folderPath):
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
                    newIm = im.resize((160,208))

                    newImPath = os.path.join(pathToSave,file)
                    #print(newImPath)
                    newIm.save(newImPath)
                #w,h = im.size
                
                #if w < minW:
                #    minW = w
                #if h < minH:
                #    minH = h
                #if w != 176 or h != 208:
                #    print("WE GOT A PROBLEM")
                #start = False
                

            
 



