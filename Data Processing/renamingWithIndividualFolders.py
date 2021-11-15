import os
import shutil


rotatedFolder = r"C:\Users\const\Desktop\Data_Processing\ALL\rotated"
folderNames = ["1yr_1.5","1yr_3","2yr_1.5","2yr_3","3yr_1.5","3yr_3"]
folderNames = ["base_2yr_3","base_3"]
#folderNames = ["test"]
start = True

for i in folderNames:
  folderPath = os.path.join(rotatedFolder,i)
  print(folderPath)
  for root, dirs, files in os.walk(folderPath):
    for file in files:
        ending = file[-4:]
        if ending == ".jpg":
            '''
            #if start:
            #print(file)
            idName = file[:-4]
            #print(idName)
            #print(pos)
            newName = idName + "_"+i+ending
            #print(newName)
            '''

            posUnderscore = file.rfind("_")
            #print(pos)
            newName = file[posUnderscore+1:]
            #print(newName)
            posDash = newName.rfind("-")
            #print(posDash)
            newName = newName[:posDash]
            #print(newName)
            newName = newName+ "_"+i+ending
            #print(newName)
            
            

            currentPath = os.path.join(root,file)
            newpath = os.path.join(root,newName)
            #print(currentPath)
            #print(newpath)
            os.rename(currentPath,newpath)
            #print("---------")
            



