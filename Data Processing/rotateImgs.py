from scipy import ndimage, misc
import imageio
import numpy as np
import os


dataProcFolder = r"C:\Users\const\Desktop\Data_Processing\ALL"
rotatedFolder = r"C:\Users\const\Desktop\Data_Processing\ALL\rotated"
folderNames = ["1yr_1.5","1yr_3","2yr_1.5","2yr_3","3yr_1.5","3yr_3"]
#folderNames = ["3yr_3"]
for i in folderNames:
  sliceFolderName = i+"_slices"
  inputFolderPath = os.path.join(dataProcFolder,sliceFolderName)
  outputFolderPath = os.path.join(rotatedFolder,i)
  print(inputFolderPath)
  print(outputFolderPath)
  
  for image in os.listdir(inputFolderPath):
    # create the full input path and read the file
    input_path = os.path.join(inputFolderPath,image)
    #print(input_path)
    image_to_rotate = imageio.imread(input_path)

    # rotate the image
    rotated = ndimage.rotate(image_to_rotate, 90)

    # create full output path, 'example.jpg' 
    # becomes 'rotate_example.jpg', save the file to disk
    fullpath = os.path.join(outputFolderPath, 'rotated_'+image)
    #print(fullpath)
    imageio.imwrite(fullpath, rotated)


'''
#FOR SOME REASON, THE ROTATED PICTURES GET CHOPPED OFF
# pip install Pillow if you don't already have it

# import image utilities
from PIL import Image

# import os utilities
import os

# define a function that rotates images in the current directory
# given the rotation in degrees as a parameter
def rotateImages(rotationAmt):
  # for each image in the current directory
  #for image in os.listdir(os.getcwd()):
  rel_path = "allXSlices"
  imageDirectory = os.path.join(os.getcwd(),rel_path)
  print(imageDirectory)
  for image in os.listdir(imageDirectory):
    # open the image
    print(image)
    image = os.path.join(rel_path,image)
    img = Image.open(image)
    # rotate and save the image with the same filename
    img.rotate(rotationAmt).save(image)
    # close the image
    img.close()
    
# examples of use
rotateImages(90)
'''