import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

csv_path = r"D:\CS 230\CS230_FinalProject\Final CSV Files and Data\final_binary.csv"
df = pd.read_csv(csv_path)

numpyArray = df.to_numpy()
#print(numpyArray)
#print(numpyArray.shape)
X = numpyArray[:,0]
y = numpyArray[:,1]
#print(X)
#print(y)
print(X.shape)
print(y.shape)

X_trainDev, X_test, y_trainDev, y_test = train_test_split(X,y, test_size=0.15)

print(X_test.shape)
print(y_test.shape)

dfTest = pd.DataFrame({'imageName':X_test, 'labels':y_test}, columns=["imageName", "labels"])
print(dfTest)

X_train, X_dev, y_train, y_dev = train_test_split(X_trainDev, y_trainDev, test_size=(3/17))

print(X_dev.shape)
print(y_dev.shape)
print(X_train.shape)
print(y_train.shape)

dfDev = pd.DataFrame({'imageName':X_dev, 'labels':y_dev}, columns=["imageName", "labels"])
print(dfDev)

dfTrain = pd.DataFrame({'imageName':X_train, 'labels':y_train}, columns=["imageName", "labels"])
print(dfTrain)

dfTest.to_csv("testSet.csv", index=False)
dfDev.to_csv("devSet.csv", index=False)
dfTrain.to_csv("trainSet.csv", index=False)
