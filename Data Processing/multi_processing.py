import numpy as np
import pandas as pd
import os
import sys
import cv2

multi_path = r"D:\CS 230\CS230_FinalProject\Data CSV Files\FullBaselineMulti_Dataset.csv"
multi_df= pd.read_csv(multi_path, header=0)

out_path = r"D:\CS 230\CS230_FinalProject\Data CSV Files\MultiSplits"

def main(file):
    path = r"D:\CS 230\CS230_FinalProject\Data CSV Files\BinarySplits" + "\\" + file
    df = pd.read_csv(path, header=0)

    for index, row in df.iterrows():
        multi_index = multi_df.loc[multi_df['ID'] == row["imageName"]].index.tolist()[0]
        multi_label = multi_df.loc[multi_index, "Class_Labels"]
        df.loc[index, "labels"] = multi_label

    df.to_csv(out_path + '\\' + file, index=False)


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("You only need one argument from the following: TRAIN, DEV, TEST")
    elif sys.argv[1] not in ["TRAIN", "train", "DEV", "dev", "TEST", "test"]:
        print("You only need one argument from the following: TRAIN, DEV, TEST")
    else:
        arg1 = ""
        if sys.argv[1] == "TRAIN" or sys.argv[1] == "train":
            arg1 = "trainSet.csv"
        if sys.argv[1] == "DEV" or sys.argv[1] == "dev":
            arg1 = "devSet.csv"
        if sys.argv[1] == "TEST" or sys.argv[1] == "test":
            arg1 = "testSet.csv"
        main(arg1)