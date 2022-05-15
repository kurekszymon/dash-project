import pandas as pd

df = pd.read_csv("final_dataset_head.csv", header=[1])

print(df.columns)
print(df["Date"])
