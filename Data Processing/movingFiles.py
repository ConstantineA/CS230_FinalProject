import os
import shutil

#path =r"C:\Users\const\Desktop\ADNI_Annual_2Yr_3T"
path = r"C:\Users\const\Desktop\adniBaseline"

start = True
for root, dirs, files in os.walk(path):
    for file in files:
        ending = file[-4:]
        if ending == ".jpg":
            #if start:
            print(file)
            posUnderscore = file.rfind("_")
            #print(pos)
            newName = file[posUnderscore+1:]
            #print(newName)
            posDash = newName.rfind("-")
            #print(posDash)
            newName = newName[:posDash]
            #print(newName)
            newName = newName + ending
                #print(newName)
                #start = False
            

            currentPath = os.path.join(root,file)
            newpath = os.path.join(root,newName)
            #print(currentPath)
            #print(newpath)
            os.rename(currentPath,newpath)
            #print("---------")
            



