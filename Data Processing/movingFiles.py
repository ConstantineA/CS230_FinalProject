import os
import shutil

path =r"C:\Users\const\Desktop\School\Coterm Year\1st Quarter\CS 230\Final_Project\ADNI1_Annual\ADNI"

if os.path.exists(r"C:\Users\const\Desktop\School\Coterm Year\1st Quarter\CS 230\Final_Project\ADNI1_Annual\ADNI\127_S_0622\MPR__GradWarp__B1_Correction__N3__Scaled\2007-06-27_13_12_00.0\I72352\ADNI_127_S_0622_MR_MPR__GradWarp__B1_Correction__N3__Scaled_Br_20070910193313383_S34177_I72352.nii"):
    print("File exists")
else:
    print("FILE DOESN'T EXIST")

for root, dirs, files in os.walk(r"C:\Users\const\Desktop\School\Coterm Year\1st Quarter\CS 230\Final_Project\ADNI1_Annual\ADNI\127_S_0622\MPR__GradWarp__B1_Correction__N3__Scaled\2007-06-27_13_12_00.0\I72352"):
    for file in files:
        print(file)


if os.path.exists(r"C:\Users\const\Desktop\School\Coterm Year\1st Quarter\CS 230\Final_Project\ADNI1_Annual\ADNI\127_S_0622\MPR__GradWarp__B1_Correction__N3__Scaled\2007-06-27_13_12_00.0\I72352\ADNI_127_S_0622_MR_MPR__GradWarp__B1_Correction__N3__Scaled_Br_20070910193313383_S34177_I72352.nii"):
    print("File exists")
else:
    print("FILE DOESN'T EXIST")


# #we shall store all the file names in this list
# filelist = []

# for root, dirs, files in os.walk(path):
#     for file in files:
#         #append the file name to the list
#         #print(file)
#         currFile = os.path.join(root,file)
#         #print(currFile)
#         specFile = r"C:\Users\const\Desktop\School\Coterm Year\1st Quarter\CS 230\Final_Project\All_Files"
#         newcurrFile = r'%s' % currFile
#         print(newcurrFile)
#         if newcurrFile == specFile:
#             print("we have a match")
        # if os.path.exists(file):
        #     print("File exists")
        # else:
        #     print("FILE DOESN'T EXIST")
        # ending = currFile[-3:]
        # if ending == "nii":
        #     #print(currFile)
        #     #print(name)
        #     pos = currFile.rfind("_")
        #     #print(pos)
        #     newName = currFile[pos+1:]
        #     #print(newName)
        #     newFolder = r"C:\Users\const\Desktop\School\Coterm Year\1st Quarter\CS 230\Final_Project\PythonMovedFiles"
        #     newPath = os.path.join(newFolder, newName)
            
        #     #os.rename(currPath, newPath)
        #     #os.replace(currPath, newPath)
        #     #print(currFile)
        #     #print(newPath)
        #     shutil.move(currFile,newPath)

        # filelist.append(os.path.join(root,file))


# #print all the file names
# for name in filelist:
#     if name[-3:] == "nii":
#         #print(name)
#         pos = name.rfind("_")
#         #print(pos)
#         newName = name[pos+1:]
#         #print(newName)
#         currPath = name
#         newFolder = r"C:\Users\const\Desktop\School\Coterm Year\1st Quarter\CS 230\Final_Project\PythonMovedFiles"
#         newPath = os.path.join(newFolder, newName)
        
#         #os.rename(currPath, newPath)
#         #os.replace(currPath, newPath)
#         print(currPath)
#         print(newPath)
#         shutil.move(currPath,newPath)
#         #print(os.path.join(path, "User/Desktop", ))
# print(len(filelist))

# #for path, subdirs, files in os.walk(root):
#    for name in files:
#        print os.path.join(path, name)
