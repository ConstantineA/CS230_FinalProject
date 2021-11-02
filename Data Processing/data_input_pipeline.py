import numpy as np
import pandas as pd
import os
import sys
import cv2
import pickle


image_path = r"D:\CS 230\CS230_FinalProject\allBaselineImages"

def main(file, output_file):
    path =r"D:\CS 230\CS230_FinalProject\Data CSV Files\BinarySplits" + "\\" + file
    df = pd.read_csv(path, header=0)
    X = []
    Y = []
    for _, row in df.iterrows():
        im = cv2.imread(image_path+"\\"+row["imageName"]+".jpg")
        X.append(im)
        Y.append(row["labels"])

    X = np.array(X)
    Y = np.array(Y)
    X_file = output_file + "X.p"
    Y_file = output_file + "Y.p"

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
            arg2 = "train_"
        if sys.argv[1] == "DEV" or sys.argv[1] == "dev":
            arg1 = "devSet.csv"
            arg2 = "dev_"
        if sys.argv[1] == "TEST" or sys.argv[1] == "test":
            arg1 = "testSet.csv"
            arg2 = "test_"
        main(arg1, arg2)