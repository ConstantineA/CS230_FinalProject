import os
import shutil
import pandas as pd


# csv = r"D:\CS 230\CS230_FinalProject\ADNI CSVs\ADNI1_Complete_3Yr_3T_11_14_2021.csv"
# out_csv = r"D:\CS 230\CS230_FinalProject\ADNI CSVs\8.csv"
# folderNames = ["1yr_1.5","1yr_3","2yr_1.5","2yr_3","3yr_1.5","3yr_3"]
# folderNames = ["base_2yr_3","base_3"]
# #folderNames = ["test"]
# start = True

# df = pd.read_csv(csv, header=0)
# df = df[df['CDR'].notna()]

# for index, row in df.iterrows():
#     row["ID"] = row["ID"] + "_3yr_3"
#     val = 0
#     if row["CDR"] == "MCI":
#       val = 1
#     elif row["CDR"] == "AD":
#       val = 2
#     row["CDR"] = val

# print(df.head())


# df.to_csv(out_csv, index=False)

path = r'D:\CS 230\CS230_FinalProject\ADNI CSVs' # use your path

li = []

for i in range(1, 9):
  filename = path + "\\" + str(i) + ".csv"
  df = pd.read_csv(filename, index_col=None, header=0)
  li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

out_csv = r'D:\CS 230\CS230_FinalProject\ADNI CSVs\adni_complete.csv'
frame.to_csv(out_csv, index=False)