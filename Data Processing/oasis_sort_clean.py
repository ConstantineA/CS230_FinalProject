import os
import pandas as pd

path =r"D:\CS 230\OASIS\oasis_images"

df = pd.read_csv("D:\CS 230\OASIS\oasis_cross-sectional.csv", header=0)
df = df[df['CDR'].notna()]
patients = list(df["ID"])

for count, filename in enumerate(os.listdir(path)):
        patient = filename[:13]
        dst = path + "\\" + patient + ".gif"
        if patient not in patients:
            os.remove(dst)
