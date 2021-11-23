from os.path import exists
import pandas as pd

csv_path = r"D:\CS 230\CS230_FinalProject\final_multi.csv"
out_csv = r"D:\CS 230\CS230_FinalProject\final_binary.csv"

full_df = pd.read_csv(csv_path, header=0)
for index, row in full_df.iterrows():
    if int(row["CDR"]) != 0:
        full_df.at[index, 'CDR'] = 1
full_df.to_csv(out_csv, index=False)