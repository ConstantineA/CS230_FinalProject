import numpy as np
import pandas as pd
import sys
import cv2
import pickle


image_path = r"C:\Users\const\Desktop\allComplete_ForResNet"

def main(file, output_file):
    path = r"C:\Users\const\Desktop\multiSplits\\" + file
    df = pd.read_csv(path, header=0)
    X = []
    Y = []
    for _, row in df.iterrows():
        im = cv2.imread(image_path+"\\"+row["imageName"]+".jpg")
        #print(im.shape)
        X.append(im)
        Y.append(row["labels"])

    X = np.array(X)
    print(X.shape)
    Y = np.array(Y)
    out_path = r"C:\Users\const\Desktop\multiSplits\\"
    X_file = out_path + output_file + "X.p"
    Y_file = out_path + output_file + "Y.p"

    pickle.dump(X, open( X_file, "wb" ) )
    pickle.dump(Y, open( Y_file, "wb" ) )

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("You only need one argument from the following: TRAIN, DEV, TEST")
    elif sys.argv[1] not in ["TRAIN", "train", "DEV", "dev", "TEST", "test"]:
        print("You only need one argument from the following: TRAIN, DEV, TEST")
    else:
        arg1 = ""
        arg2 = ""
        if sys.argv[1] == "TRAIN" or sys.argv[1] == "train":
            arg1 = "trainSet.csv"
            arg2 = "trainRes_"
        if sys.argv[1] == "DEV" or sys.argv[1] == "dev":
            arg1 = "devSet.csv"
            arg2 = "devRes_"
        if sys.argv[1] == "TEST" or sys.argv[1] == "test":
            arg1 = "testSet.csv"
            arg2 = "testRes_"
        main(arg1, arg2)