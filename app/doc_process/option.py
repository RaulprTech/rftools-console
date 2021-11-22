import pandas as pd
import glob


files = glob.glob("input/" + "*.s2p")

frames = []

for f in files:

    data = pd.read_table(f, comment="!")
    
    frames.append(data)

    print(data)

df = pd.concat(frames, ignore_index=True)
# print(df)
# df.to_csv("Output/parameters.csv", header=True, sep=";")
